
from typing import Optional,List
from fastapi import Depends,FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models,schemas,utils
from .routes import post,user


from .database import engine,get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app=FastAPI()



while True:
    try:
        conn=psycopg2.connect(host='localhost',database='pybackend',
                              user='postgres',
                              password='bidyut',
                              cursor_factory=RealDictCursor)
        cursor=conn.cursor()    
    
        print("Database connection was successful")
        break
    except Exception as error:
        print("Failed to connect to database")
        print("Error:",error)
        time.sleep(2)
       
    
 
app.include_router(post.router)
app.include_router(user.router)
 
    
    