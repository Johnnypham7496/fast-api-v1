from fastapi import Response, Depends, APIRouter, status, HTTPException
from repository import users_repository
from db_config import get_db
from sqlalchemy.orm import Session
from schemas import UserModel, MessageModel, CreateUserModel
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


@router.post("/", response_description="Successfully created user", description="Creates a user", response_model= UserModel, status_code= status.HTTP_201_CREATED, responses= {400: {"model": MessageModel}})
def add_user(request: CreateUserModel, response: Response, db: Session = Depends(get_db)):
    username_request = request.username
    email_request = request.email
    role_request = request.role

    if username_request.strip() == "":
        response_text = "username field cannot be empty. Please check your payload and try again"
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=response_text)
    
    if email_request.strip() == "":
        response_text = "email field cannot be empty. Please check your payload and try again"
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=response_text)
    
    if role_request.strip() == "":
        response_text = "role field cannot be empty. Please check your payload and try again"
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail=response_text)
    

    response.status_code = status.HTTP_201_CREATED
    response.headers['Location'] = '/users/v1/' + str(username_request.strip())
    return users_repository.add_user(db, username_request.strip(), email_request.strip(), role_request.strip())


@router.post('/{username}', response_description='Successfully updated user info', description='Update a single user record', status_code=204, responses={204: {"message": None}, 400: {"message": MessageModel}, 404: {"message": MessageModel}})
def update_user(username: str, request: UserModel, response: Response, db: Session = Depends(get_db)):
    email_request = request.email
    role_request = request.role

    if email_request == None and role_request == None:
        response_text = 'request body cannot be empty. Please check your payload and try again'
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= response_text)
    
    user_check = users_repository.get_by_username(db, username)

    if user_check == None:
        response_text = 'username not found. Please use Post to create a user record'
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response_text)
    
    if email_request != "":
        email_request = email_request.strip()
    else: 
        email_request = ""

    if role_request != None:
        role_request = role_request.strip()
    else: 
        role_request = ""

    
    if email_request == "" and role_request == "":
        response_text = 'request body fields cannot be empty. Please check you payload and try again'
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response_text)
    
    response.status_code= status.HTTP_204_NO_CONTENT
    return users_repository.update_user(db, username, email_request, role_request)