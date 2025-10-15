from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import Depends,HTTPException,status
from . import JWTtoken


#Creating an instance of OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") #tokenUrl mein routers folder ke authentication.py file mein jaha create token hota hai after entering correct credentials uska naam dena hota hai

#basically upar waale line ka matlab hai from (where/which url) you want to fetch the token?


#STEP 5
#Create a function get_current_user


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    #Step 7 is to call and return verify_token() function here
    return JWTtoken.verify_token(token,credentials_exception) #we pass credentials_exception from here , because we need to use that exception in our JWTtoken.py file's verify_token function definition

    #Step 8 is to add this current user to the neede api
    
    
#STEP 6 is again in JWTtoken.py