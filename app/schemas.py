


from datetime import datetime
from typing import Optional
from pydantic import BaseModel,EmailStr

# BaseModel validates the data provided by the client and provides a way to convert it to JSON.

#  user input should be like.
class UserCreate(BaseModel):
    email:EmailStr
    password:str
    
# user response should be like.
class UserResponse(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    # password:str


# user login
class UserLogin(BaseModel):
    email:EmailStr
    password:str


class PostBase(BaseModel):
    title: str
    content:str
    published:bool=True


class PostCreate(PostBase):
    pass
    

class Post(PostBase):
    created_at:datetime 
    id:int
    user_id:int
    user:UserResponse
    # class Config:
    #     orm_mode=True



# Token
class Token(BaseModel):
    access_token: str
    token_type: str
    

# Token data
class TokenData(BaseModel):
    id: Optional[str]=None
