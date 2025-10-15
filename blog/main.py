from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import schemas # . means that from the same Directory
from . import models,hashing
from typing import List
from .database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from . routers import blog,user,authentication
app=FastAPI()


models.Base.metadata.create_all(engine)


#This is done to include the routers to our main.py file
app.include_router(blog.router) #name of router file blog.py plus .router

app.include_router(user.router)

app.include_router(authentication.router)
 

# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['Blog'],response_model=schemas.ResponseSchemaOfBlog)  #Jo status code hame dikhana hota hai woh hum apne app decorator mein hi dikhaate hai
# def create(request:schemas.Blog,db:Session=Depends(get_db)): #But we do not want to simply pass variables like this
#     # def create(title,body):
# # we want to do it through pydantic by making a class and passing that here
#     # return {'data':{'message':'Creating',
#     #                 'title':request.title,
#     #                 'body':request.body}}
    
#     new_blog=models.Blog(title=request.title,body=request.body,user_id=1) #after making relationship with user, just manually assigning user_id to 1 here for checking purpose
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# #Now making a delete api
# @app.delete('/blog/{id}',status_code=status.HTTP_200_OK,tags=['Blog'])
# def destroy(id:int,response:Response,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} does not exist')
#     blog.delete(synchronize_session=False)
    
#     #Why we do the above before delete is explained in the update API
    
#     #This is not yet deleted , when we do any changes in the db like create, update or delete , we should do
#     # db.commit()
#     db.commit()
#     return {'details':{'message':f'blog with id {id} is deleted'}}

# #Now Making an Update api
# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['Blog'])
# def update(id:int,response:Response,request:schemas.Blog,db:Session=Depends(get_db)):
#     #blog=db.query(models.Blog).filter(models.Blog.id==id).update({'title':request.title})  
    
#     #Yha ek ek krke title fir body ,fir aur bhi dusre fields ko likhne se achha hai ki hum update mein sidhe request schema hi send kr de
    
#     #Kyuki koi field agar chhut gya ek ek krke likhne mein , toh woh update bhi nhi hoga
#     blog=db.query(models.Blog).filter(models.Blog.id==id)
#     # dekh .first toh hame check krne ke liye chahiye hi, prr jab hum update krte hai tab .first() ya .all() nhi krna hota sidhe .update() hota hai , isliye niche if not waale mein blog.first() krlo to check if it exists or not
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} does not exist')
    
#     blog.update(request.dict())  # .update() expects a dictionary only , so when we pass request , we must convert it into dict by doing .dict() at the end otherwise we get 500 internal server error
#     db.commit()
#     return 'updated'
    
    

# #Now making a get api to get all the blogs from the database

# @app.get('/blog',status_code=status.HTTP_200_OK,response_model=List[schemas.ResponseSchemaOfBlog],tags=['Blog']) #Here for getting all blogs if I simply wrote ->response_model=schemas.ResponseSchemaOfBlog , it would have given me internal server error, because for multiple responses It should be passed inside List First , which we import from typing
# def all(db:Session=Depends(get_db)):  #Here again we will pass db:Session =Depends(get_db) to get the Database INstance here
#     blogs=db.query(models.Blog).all() #yha pr database instance prr query kr rhe hai apan 
#     #to get all the blogs we just do 
#     # db.query(jis_table pr kr rhe).all()
#     return blogs



# #Now making an API for getting a particular blog based on ID

# @app.get('/blog/{id}',response_model=schemas.ResponseSchemaOfBlog,tags=['Blog']) #We include the Response Schema which is going to be shown in Response in the decorator
# def get_by_id(id:int,response:Response,db:Session=Depends(get_db)):  #response of type Response is used to give custom status code when things go wrong
#     blog=db.query(models.Blog).filter(models.Blog.id==id).first()   #filter is used like where 
#     # .first() fetches the first instance of the filter, agar yhi maine .all() kiya hota toh it would have fetched all the matching instances
    
#     if not blog:
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {'detail':f"Blog with id {id} not found"}
        
#         #The above 2 lines can be replaced to simple 1 line code using raise HTTPException
        
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} not found")
#     return blog


#Making an instance of CryptContext to use it further


# #Making API to create User 
# @app.post('/create_user',status_code=status.HTTP_201_CREATED,response_model=schemas.ResponseBodyofUser,tags=['Users'])
# def create_user(request:schemas.RequestBodyOfUser,db:Session=Depends(get_db)):

    
#     #Now before making a new_user we should hash our password first and then store it in the db using the pwd_cxt instance which we created outside
    
 
    
#     #Instead of manually assigning each field , we can simply do 
    
#     # new_user=models.User(**request.dict())
#     # here ** is a dictionary unpacking operator and .dict() to convert it into dictionary
#     '''It takes a dictionary like this:
#     data = {"name": "Siddhant", "email": "sid@gmail.com", "password": "1234"}
#     and unpacks it into separate keyword arguments like this:
#     func(name="Siddhant", email="sid@gmail.com", password="1234")'''
    
#     new_user=models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# #creating an API to get the User

# @app.get('/get_user/{id}',response_model=schemas.ResponseBodyofUser,status_code=status.HTTP_200_OK,tags=['Users']) #we use tags=['User'] or tags=['Blogs'] to segregate apis of one type together, we do it in our decorator only
# def get_user(id:int,db:Session=Depends(get_db)):
#     user=db.query(models.User).filter(models.User.id==id).first()
    
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No data corresponding to id {id} found")
    
#     return user