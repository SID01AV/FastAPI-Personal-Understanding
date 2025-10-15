from pydantic import BaseModel
from typing import List,Optional

#Making a Pydantic Request Body class
class Blog(BaseModel):
    title:str
    body:str
    
    

        
        
        
#Creating a Request Schema for Create User API 
class RequestBodyOfUser(BaseModel):
    name:str
    email:str
    password:str
    
    
#creating a Response schema for create user

class ResponseBodyofUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog] # here we are doing the same as we did in class ResponseSchemaOfBlog(Blog), by using the same exact relationship that we defined in models.py file , Blog in List[Blog] is the Schema for showing Blog
    class Config:
        orm_mode=True
        
        
        
#Creating a response body schema for Blog

class ResponseSchemaOfBlog(Blog): #Here we are inheriting from request schema , which already inherits form BaseModel
    
    
    #now I also want to show the creator who has created this blog, after building relationship btw Blog and User table
    #We should use the name of relationship that we defined only, for example we can't use 
    # created_by:ResponseBodyofUser , because
    '''
    FastAPI tries to convert models.Blog to schemas.ResponseSchemaOfBlog 

    It checks: “Does this Blog object have all the fields required by the schema?”

    It finds that created_by (in schema) doesn’t exist in your Blog model instance , becuase it's with the name creator→ 💥 error.
    '''
    creator:ResponseBodyofUser  #ResponseBodyofUser Schema use krne ke liye hame woh iss schema se pehle define krna padega, due to python's line by line execution
    class Config:
        orm_mode=True
        #we do this because By default, Pydantic models (our schemas) only know how to work with dictionaries, not ORM (SQLAlchemy) objects.

        #so this done to convert our orm object to dictionary for displaying
        
        
#Making a Schema for Login

class Login(BaseModel):
    username:str
    password:str
    
#Making a Schema for Token and TokenData as mentioned in JWTtoken.py file

class Token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
    email:Optional[str]=None