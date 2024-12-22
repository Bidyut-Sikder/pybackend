


from datetime import datetime
from typing import Optional
from pydantic import BaseModel,EmailStr,field_validator,FieldValidationInfo
# from pydantic.types import conint

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
    class Config:
        from_attributes = True



# # user login
class UserLogin(BaseModel):
    email:EmailStr
    password:str

# # posts
class PostBase(BaseModel):
    title: str
    content:Optional[str]
    published:bool=True
    
    class Config:
        from_attributes = True


class PostCreate(PostBase):
    pass
    

class Post(PostBase):
    created_at:datetime 
    id:int
    user_id:int
    user:UserResponse
    
    class Config:
        from_attributes=True

class PostOut(BaseModel): 

    post:Post
    votes:int 
    
    class Config:
     from_attributes=True

# Vote







class Vote(BaseModel):
    post_id:int
    direction:int
    @field_validator("direction")
    def validate_direction(cls, value, info: FieldValidationInfo):
        if value not in {0, 1}:
            raise ValueError("Direction must be 0 or 1")
        return value
    


# Token 
class Token(BaseModel):
    access_token: str
    token_type: str
    

# Token data
class TokenData(BaseModel):
    id: Optional[str]=None
