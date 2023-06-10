from fastapi import Response, Depends, APIRouter,status
from repository import user_repository
from db_config import get_db
from sqlalchemy.orm import Session
from schemas import UserModel

router = APIRouter(
    prefix="/users/v1",
    tags= ["users"]
)


@router.get("/", response_description="Displays all users", description="Retrieves all users", response_model=list[UserModel])
def get_all_users(resposne: Response, db: Session = Depends(get_db)):
    return_value = user_repository.get_all_users()
    resposne.status_code = status.HTTP_200_OK
    return return_value