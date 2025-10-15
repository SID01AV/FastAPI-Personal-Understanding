#We are going to implement login and oAuth Token
from fastapi import FastAPI,Depends,status,Response,HTTPException
from datetime import datetime,timedelta
from .. import schemas # .. means that from 1 directory outside the current
from .. import models,hashing,JWTtoken
from typing import List
from ..database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm


router=APIRouter(tags=["Authentication"])


@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    #Basically hum Login kyu bana rhe hai, taaki koi user apna username aur password daale toh usko hum authenticate kr paaye , ki yeh user exist krta hai ya nhi
    
    user=db.query(models.User).filter(models.User.email==request.username).first() #basically request body mein from front end hum email hi daalenge prr humne schema mein username likha hai kyuki oAuth2PasswordRequestForm username dhundh rha hota hai
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'This user is not registered with us.')
    
    #check for correct password as well
    #we make a verify method inside our Hash class of hashing.py file
    if not hashing.Hash.verify(request.password,user.password):  #request password is our plain password which we recieve from user through request schema on our frontEnd
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'You have Entered wrong Password')
    
    
    #If Everything is fine, which means that the username and password exist in the DB/User has entered correct login creds, just generate a token

    #Step 3
    
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = JWTtoken.create_access_token(
        data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}

#Step 4
#We have successfully returned Token above , NOW we need to hide the APIs behind our token

#create a file oAuth2.py in the blog directoryy\ 