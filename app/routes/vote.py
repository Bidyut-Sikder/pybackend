

from fastapi import APIRouter, FastAPI,status,Depends,HTTPException
from sqlalchemy.orm import Session
from .. import schemas,database,auth2,models
from pydantic import BaseModel, EmailStr, ValidationError
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix='/votes',tags=['Votes'])





# @router.post('/',status_code=status.HTTP_201_CREATED)
# def vote(vote:schemas.Vote,current_user:dict=Depends(auth2.get_current_user),db:Session=Depends(database.get_db)):

#  vote_query=db.query(models.Vote).filter(models.Vote.post_id==vote.post_id,models.Vote.user_id==current_user.id)
#  found_vote=vote_query.first()
 
#  if (vote.direction==1):

#   if found_vote:
#     raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="You have already voted for this post")

#   new_vote=models.Vote(post_id=vote.post_id,user_id=current_user.id)
  
#   db.add(new_vote)
#   db.commit()
  
#   return {'message':"vote added successfully."}
  
#  else: 

#     if not found_vote:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="You haven't voted for this post yet")
    
#     vote_query.delete(synchronize_session=False)
#     db.commit()
#     return {'message':"vote deleted successfully."}
    
    
    
 






@router.post('/',status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote,current_user:dict=Depends(auth2.get_current_user),db:Session=Depends(database.get_db)):
 try:
   post=db.query(models.Post).filter(models.Post.id==vote.post_id).first()

   if post==None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post not found")
  
   vote_query=db.query(models.Vote).filter(models.Vote.post_id==vote.post_id,models.Vote.user_id==current_user.id)
   found_vote=vote_query.first()
   
   if (vote.direction==1):

    if found_vote:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="You have already voted for this post")

    new_vote=models.Vote(post_id=vote.post_id,user_id=current_user.id)
   
    db.add(new_vote)
    db.commit()
   
    return {'message':"vote added successfully."}
   
   else:  
      if not found_vote:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="You haven't voted for this post yet")
      
      vote_query.delete(synchronize_session=False)
      db.commit()
      return {'message':"vote deleted successfully."}
      
    #Shows error if post does not exist.
#  except IntegrityError as e: 
#         db.rollback()  # Roll back the session to avoid invalid state
#         if "foreign key constraint" in str(e.orig):
#             raise HTTPException(
#                 status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#                 detail="Provided post_id or user_id does not exist",
#             )

 except Exception as e:
   raise e





 



 

  














