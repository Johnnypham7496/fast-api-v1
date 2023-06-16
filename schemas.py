from pydantic import BaseModel, Optional


class UserModel(BaseModel):
    id: int
    username: str
    email: str
    role: str


    class Config:
        orm_mode = True


class MessageModel(BaseModel):
    detail: str


class CreateUserModel(BaseModel):
    username: str
    email: str
    role: str


class UpdateUser(BaseModel):
    email: Optional[str]
    role: Optional[str]