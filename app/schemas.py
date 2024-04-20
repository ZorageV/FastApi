from datetime import datetime
from pydantic import BaseModel,ConfigDict, EmailStr

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass

class Post(PostBase):
    model_config = ConfigDict(from_attributes=True)


class UserCrate(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int
    email : EmailStr