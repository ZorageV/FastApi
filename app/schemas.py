from datetime import datetime
from typing import Optional
from pydantic import BaseModel,ConfigDict, EmailStr

class PostBase(BaseModel):
    title: str
    content: str
    user_id : int
    published: bool = True


class PostCreate(PostBase):
    pass

class Post(PostBase):
    id : int
    created_at : datetime
    user_id : Optional[int] 

    model_config = ConfigDict(from_attributes=True)


class UserCrate(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int
    email : EmailStr


class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int] = None