from fastapi import Response, Depends, APIRouter, status, HTTPException
from repository import users_repository
from db_config import get_db
from sqlalchemy.orm import Session
from schemas import UserModel, MessageModel
from typing import List

router = APIRouter(
    prefix="/users/v1",
    tags= ["users"]
)


@router.get("/", response_description="Display all users", description="Retrieves all users", response_model=List[UserModel])
def get_users(resposne: Response, db: Session = Depends(get_db)):
    return_value = users_repository.get_all_users(db)
    resposne.status_code = status.HTTP_200_OK
    return return_value


@router.get("/{username}", response_description="Display user by username", description="Retrieves user by username", response_model=UserModel, responses= {404: {"model": MessageModel}})
def get_by_username(response: Response, username: str, db: Session = Depends(get_db) ):
    return_value = users_repository.get_by_username(db, username)

    if return_value == None:
        response_text = "username not found. Please check your parameter and try again"
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= response_text)
    
    response.status_code = status.HTTP_200_OK
    return return_value