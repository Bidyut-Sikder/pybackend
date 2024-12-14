

from typing import List
from fastapi import HTTPException,status,Depends,APIRouter

from ..database import get_db
from .. import schemas,utils,models,main
from sqlalchemy.orm import Session
 
router=APIRouter(
    prefix='/posts',tags=['Posts']
)

# Posts Routes 
@router.get('/')
def root():
    return{"message":"hello world"}

@router.get('/{id}',response_model=schemas.Post )
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
        

        return post_query.first()
        # return {"status":"success","data":post_query.first()}
    except Exception as error:
        
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))


@router.get('/',response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute('SELECT * FROM posts')
    # posts = cursor.fetchall()
    posts=db.query(models.Post).all()
    return  posts
    # return {"data": posts}
 

@router.post('/', status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post: schemas.PostCreate,db:Session=Depends(get_db)):
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
    
         
        return  new_post
        # return {"data": new_post}
    except Exception as error:
        raise error
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

 

@router.delete('/{id}' )
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
     
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

@router.put('/{id}',response_model=schemas.Post )
def update_post(id: int,data:schemas.PostCreate,db:Session=Depends(get_db)):
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
         
         return post_query.first()
        #  return {"status":"success","data":post_query.first()}
    except Exception as error:

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))
   
   
    























