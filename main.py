from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

#create an instance if FastAPI
app=FastAPI()


@app.get('/welcome')   #here / basically means our local host at 8000 port, 
# .get is called operation in FastAPI Language , for example .post, .put are other such operations

# ('/welcome') is called the path
def index():
    # return 'heyy'  -> That's cool but FastAPI gives us the benefit of directly returning a JSON,Unlike in Django where we need to use Serializer for converting to JSON
    return {'data':{'name':'Siddhant','age':24}}

@app.get('/blog/{id}')  #apne path mein koi Dynamic variable pass krna ho to {} ke andar krte hai ->This is called path Parameter
#fir apne function mein pehle usko as a parameter pass krte hai to use inside the function
def show(id):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id:int):
    return {'data': {'id':id,'comments':['comment1','comment2']}}

# Now if you want to dictate the type of id which should be accepted, you need to do that inside the function parameter like in

#def comments(id:int):

#But there is something called Query Parameter , which helps in limiting the content to a certain number , or sending data for only those when something is true maybe, basically ? ke baad ka koi bhi logic implement hota hai woh waala query parameter hota hai, Query Parameter Optional Hota hai, prr path parameter ke bina API chal hi nhi skti
#Implementation of Query Parameter ->only passed in the function and not in the path
@app.get('/bhejo')
def bhejo(limit:int=5,published:bool=True,sort:Optional[bool]=True): #Dekho apne ko yeh filters hamesha nhi dene hote path Paramter , toh isliye hame hamesha koi default value deni chahiye
    if published:
         
        return {'data':f'{limit} published documents bhej do sorted {sort} hai'}
            
    else:
        return {'data':f'No Published Documents found'}
    

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]=None
    
@app.post('/blog')
def create_blog(request:Blog):
    return {'data':f"Blog is created with title {request.title}"}
    