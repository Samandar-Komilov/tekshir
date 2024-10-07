from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr
    phone: str
    username: str


class UserCreate(BaseModel):
    password: str


class UserInDB(BaseModel):
    id: int
    hashed_password: str


class UserInPublic(BaseModel):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None