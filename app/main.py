
from typing import Optional
from fastapi import Depends,FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models

from .database import engine,get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)



app=FastAPI()



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
    posts=db.query(models.Post).all()
  
    return {"status": "success","data":posts}


@app.get('/posts/{id}' )
def get_by_id(id: int,db:Session=Depends(get_db)):
    try:
       
        # cursor.execute('SELECT * FROM posts WHERE id = %s ', (id,))
        # post = cursor.fetchone()
        # if post==None:
        #  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not found")
        
        # return {"status":"success","data":post}
        post_query=db.query(models.Post).filter(models.Post.id==id)
        

        if post_query.first()==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not found")
        

        return {"status":"success","data":post_query.first()}
    except Exception as error:
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))


@app.get('/posts')
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute('SELECT * FROM posts')
    # posts = cursor.fetchall()
    posts=db.query(models.Post).all()
    return {"data": posts}





@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post,db:Session=Depends(get_db)):
    try:
        # val = (post.title, post.content, post.published)
        # cursor.execute('INSERT INTO posts (title, content, published) VALUES(%s, %s, %s) RETURNING *', val)
        # new_post = cursor.fetchone()
        # conn.commit()
        new_post=models.Post(
            title=post.title,content=post.content,published=post.published)
        
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
    
         
        return {"data": new_post}
    except Exception as error:
        raise error
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

 

@app.delete('/posts/{id}' )
def delete_post(id: int,db:Session=Depends(get_db)):
    try:
       
        # cursor.execute('DELETE FROM posts WHERE id = %s RETURNING *', (id,))
        # post = cursor.fetchone()
        # conn.commit()
        post=db.query(models.Post).filter(models.Post.id==id)
       
        if post.first()==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not found")
        
        post.delete()
        db.commit()
        return {"status":"success","message":"deleted successfully."}
    except Exception as error:
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

@app.put('/posts/{id}' )
def update_post(id: int,data:Post,db:Session=Depends(get_db)):
    try:
        # val=( data.title,data.content,data.published,id)
        # cursor.execute('UPDATE  posts SET title=%s,content=%s,published=%s  WHERE id = %s RETURNING *',val)
        # post = cursor.fetchone()
        # conn.commit()
        # if post==None:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not found")
        
        # return {"data": post}
        
         post_query=db.query(models.Post).filter(models.Post.id==id)
      
         post=post_query.first()
         if post==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not found")
        #{"title":data.title,"content":data.content,"published":data.published}
         post_query.update(dict(data),synchronize_session=False)
         db.commit()
         
         return {"status":"success","data":post_query.first()}
    except Exception as error:
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

