
from typing import Optional,List
from fastapi import FastAPI
from . import config
from fastapi.middleware.cors import CORSMiddleware


from psycopg2.extras import RealDictCursor

from . import models,schemas,utils
from .routes import post,user,auth,vote


from .database import engine,get_db
from sqlalchemy.orm import Session

# creates all the database tables
# instead of using this we will use alembic to create database tables

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

# Adding middleware cors to enable cross origin resource sharing

origins=[
 "https://github.com",
    "https://chatgpt.com",
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.typescriptlang.org",
    "https://www.w3schools.com",
    "https://www.perplexity.ai"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], # To allow all origins or domains
    # allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"] 
)
 
@app.get('/')
def root():
    return {"message": "Welcome to my API." }
  
  
app.include_router(post.router)
app.include_router(user.router) 
app.include_router(auth.router)
app.include_router(vote.router)
 

