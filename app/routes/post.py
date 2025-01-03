

from typing import List, Optional
from fastapi import HTTPException,status,Depends,APIRouter
from sqlalchemy import func
import json
from ..database import get_db
from .. import schemas,utils,models,main
from sqlalchemy.orm import Session
from .. import auth2
 
router=APIRouter(prefix='/posts',tags=['Posts'])



@router.get('/{id}',response_model=schemas.PostOut )
def get_by_id(id: int,db:Session=Depends(get_db),current_user:int=Depends(auth2.get_current_user)):
  
    try:

        post = db.query(
        models.Post,
        func.count(models.Vote.post_id).label('votes')
         ).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True
        ).group_by(
            models.Post.id
        ).filter(models.Post.id==id).first()

        if post==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not found")

        return {
            "post":schemas.Post.model_validate(post[0]),  # SQLAlchemy model to Pydantic
            "votes":post[1]
        }
        
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))



@router.get('/',response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db),current_user:int=Depends(auth2.get_current_user),
              limit:int=None,
              skip:int=None,
              search:str=''
              ):
   
    posts = db.query(
        models.Post,
        func.count(models.Vote.post_id).label('votes')
    ).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True
    ).group_by(
        models.Post.id
    ).filter(
        models.Post.title.contains(search)
    ).limit(
        limit
    ).offset(
        skip
    ).all()

    serialized = [
        {
            "post": {                
                "title": post.title,
                "content": post.content,
                "published": post.published,
                "created_at": post.created_at,
                "id": post.id,
                "user_id": post.user_id,
                "user": {
                    "id": post.user.id,
                    "email": post.user.email,
                    "created_at": post.user.created_at
                }
            },
            "votes": votes
        }
        for post,votes in posts
    ]
    return serialized



@router.post('/', status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post: schemas.PostCreate,db:Session=Depends(get_db),current_user:int=Depends(auth2.get_current_user)):
    try:   
        new_post=models.Post(
            user_id=current_user.id,
            **dict(post)
            )
        db.add(new_post)
        db.commit()
        db.refresh(new_post) 
        return  new_post
    
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

 

# @router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT )
@router.delete('/{id}' )
def delete_post(id: int,db:Session=Depends(get_db),current_user:int=Depends(auth2.get_current_user)):

        post=db.query(models.Post).filter(models.Post.id==id)
       
        if post.first()==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not found")
         
        if post.first().user_id!=current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not authorized to perform requested action")
        
        post.delete()
        db.commit()
        
        return {"status":"success","message":"deleted successfully."}

@router.put('/{id}',response_model=schemas.Post )
def update_post(id: int,data:schemas.PostCreate,db:Session=Depends(get_db),current_user:int=Depends(auth2.get_current_user)):


         post_query=db.query(models.Post).filter(models.Post.id==id)
      
         post=post_query.first()
         
         if post==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not found")

         print(post.user_id,current_user.id)
         if post.user_id!=current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not authorized to perform requested action")
        
         
         post_query.update(dict(data),synchronize_session=False)
         db.commit()
         
         return post_query.first()
        #  return {"status":"success","data":post_query.first()}

    



mylist=[{'id':3,'name':'bidyut'},{'id':4,'name':'rajeeb'},{'id':8,'name':'sikder'}]
mylistt=['bidyut','sikder']
mydict={'name':'fdfdf'}
myset={'bidyut','sikder'}
print(mylist[0]['id'])
















