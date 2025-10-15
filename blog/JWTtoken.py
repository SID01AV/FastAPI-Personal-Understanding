from datetime import datetime, timedelta, timezone
from . import schemas
from jose import JWTError,jwt
#STEP 1
#We JUST Simply need to make a JWTtoken.py file and declare the below 3 variables first
SECRET_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30


#STEP 2
#After that we need to create 2 pydantic Models/Schema -> Token and TokenData in the schemas.py file

#After that I simply Copied the below function from fastapi.tiangolo.com page,type jwt token you will get it

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#Now pasted 3 more lines of Code in the authentication.py routing


def verify_token(token:str,credentials_exception): #credentials_exception is coming from oAuth2.py file where we have already decalred this
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception