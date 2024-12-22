
from typing import Optional,List
from fastapi import FastAPI
from . import config



from psycopg2.extras import RealDictCursor

from . import models,schemas,utils
from .routes import post,user,auth,vote


from .database import engine,get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

 

  
 
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
 
     
