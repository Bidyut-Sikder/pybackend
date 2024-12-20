from fastapi import HTTPException,status,Depends,APIRouter

from app.database import get_db
from .. import schemas,utils,models,main
from sqlalchemy.orm import Session

router=APIRouter(prefix="/users",tags=['Users'])
#tags=['Users'] to make groups on http://127.0.0.1:8000/docs 


#  User routes   
# crete user
@router.post('/', status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_user(user_data:schemas.UserCreate,db:Session=Depends(get_db)):
   try:
    # comment: 
    
    user_data.password=utils.get_password_hash(user_data.password)
    
    new_user=models.User(
        **dict(user_data)
        # email=user_data.email,password=user_data.password
        )
        
    db.add(new_user) 
    db.commit() 
    db.refresh(new_user)  
    
    return new_user

   except Exception as error:
    

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

    

# get user by id
    
    
@router.get('/{id}',response_model=schemas.UserResponse )
def create_user(id:int,db:Session=Depends(get_db)):
   try:
    # comment: 
    
    get_user=db.query(models.User).filter(models.User.id==id).first()
    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")

    return get_user

   except Exception as error:
    

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

    
































