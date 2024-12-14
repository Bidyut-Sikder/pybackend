


from datetime import datetime
from pydantic import BaseModel,EmailStr


class PostBase(BaseModel):
    title: str
    content:str
    published:bool=True


class PostCreate(PostBase):
   pass
    

class Post(PostBase):
    created_at:datetime
    id:int
    # class Config:
    #     orm_mode=True

#  user input should be like.
class UserCreate(BaseModel):
    email:EmailStr
    password:str
    
# user response should be like.
class UserResponse(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime








