
from typing import Optional
from fastapi import Depends,FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models

from .database import engine,SessionLocal
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)



app=FastAPI()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Post(BaseModel):
    title: str
    content:str
    published:bool=True


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
       
    


@app.get('/')
def root():
    return{"message":"hello world"}




app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='pybackend',
            user='postgres',
            password='bidyut',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Failed to connect to database")
        print("Error:", error)
        time.sleep(2)

@app.get('/')
def root():
    return {"message": "hello world"}

@app.get('/sqlalchemy')
def test_posts(db: Session = Depends(get_db)):
    return {"status": "success"}

@app.get('/posts')
def get_posts():
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    return {"data": posts}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    try:
        val = (post.title, post.content, post.published)
        cursor.execute('INSERT INTO posts (title, content, published) VALUES(%s, %s, %s) RETURNING *', val)
        post = cursor.fetchone()
        conn.commit()
        return {"data": post}
    except Exception as error:
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

# @app.get('/posts/{id}')
# def get_post(id: int):
#     cursor.execute('SELECT * FROM posts WHERE id = %s', (id,))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
#     return {"data": post}

# @app.put('/posts/{id}')
# def update_post(id: int, post: Post):
#     try:
#         cursor.execute('SELECT * FROM posts WHERE id = %s', (id,))
#         existing_post = cursor.fetchone()
#         if not existing_post:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
#         val = (post.title, post.content, post.published, id)
#         cursor.execute('UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *', val)
#         post = cursor.fetchone()
#         conn.commit()
#         return {"data": post}
#     except Exception as error:
#         conn.rollback()
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

# @app.delete('/posts/{id}')
# def delete_post(id: int):
#     try:
#         cursor.execute('SELECT * FROM posts WHERE id = %s', (id,))
#         post = cursor.fetchone()
#         if not post:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
#         cursor.execute('DELETEdef test_posts(db:Session=Depends(get_db)):
#         return {"status":"success"}




# @app.get('/posts')
# def get_posts():
#     cursor.execute('SELECT * FROM posts')
#     posts=cursor.fetchall()
#     return {"data":posts}



# @app.post('/posts',status_code=status.HTTP_201_CREATED)
# def create_posts(post:Post):
    
#     val=(post.title,post.content,post.published)
#     cursor.execute('INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING *',val)
#     post=cursor.fetchone()
#     return {"data":post}











