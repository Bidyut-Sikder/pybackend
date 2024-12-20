from datetime import datetime, timedelta, timezone
from typing import Annotated
from sqlalchemy.orm import Session
from . import database
from . import models


import jwt
from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel, ValidationError

from . import schemas

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60







pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login",
    # scopes={"me": "Read information about the current user.", "items": "Read items."},
)

app = FastAPI()




def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



# verify_accessToken

def verify_access_token(token: str, credentials_exception):
 
 try:
    # comment: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    
        user_id=str(payload.get('user_id'))

        if  user_id is None:
         raise credentials_exception
    

        token_data=schemas.TokenData(id=user_id)
        return token_data
 except jwt.PyJWTError as e :

    raise credentials_exception
 

# end try




def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],db:Session=Depends(database.get_db)):

   credentials_exception=  HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
   token_data=verify_access_token(token, credentials_exception)
#    print(token_data.id)
   user=db.query(models.User).filter(models.User.id==token_data.id).first()
  
   
   return user























































