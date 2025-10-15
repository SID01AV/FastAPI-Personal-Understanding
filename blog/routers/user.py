from fastapi import FastAPI,Depends,status,Response,HTTPException
from .. import schemas # .. means that from 1 directory outside the current
from .. import models,hashing
from typing import List
from ..database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter



#We learnt about routing in our blog.py router file , but what are the real benefits of routing?
'''
1)We can use tags while creating the instance of router, so we don't need to it at multiple places

2)We can set prefix for base url address , matlab jaise user ki saari api in our decorator starts with /user/and_then_something , so we can simply set that /user as prefix
'''
router=APIRouter(prefix='/user',tags=["User"])


#Making API to create User 
@router.post('/create_user',status_code=status.HTTP_201_CREATED,response_model=schemas.ResponseBodyofUser)
def create_user(request:schemas.RequestBodyOfUser,db:Session=Depends(get_db)):

    
    #Now before making a new_user we should hash our password first and then store it in the db using the pwd_cxt instance which we created outside
    
 
    
    #Instead of manually assigning each field , we can simply do 
    
    # new_user=models.User(**request.dict())
    # here ** is a dictionary unpacking operator and .dict() to convert it into dictionary
    '''It takes a dictionary like this:
    data = {"name": "Siddhant", "email": "sid@gmail.com", "password": "1234"}
    and unpacks it into separate keyword arguments like this:
    func(name="Siddhant", email="sid@gmail.com", password="1234")'''
    
    new_user=models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




#creating an API to get the User

@router.get('/get_user/{id}',response_model=schemas.ResponseBodyofUser,status_code=status.HTTP_200_OK) #we use tags=['User'] or tags=['Blogs'] to segregate apis of one type together, we do it in our decorator only
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No data corresponding to id {id} found")
    
    return user