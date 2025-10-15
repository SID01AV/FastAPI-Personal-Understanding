from .database import Base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__="blogs"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    #learning relationship and foreignKey
    
    #Making user_id foreign key 
    user_id=Column(Integer,ForeignKey('users.id'))# In  ForeignKey('real tablename not the Table's class name.jo_bhi_field_foreignkey_banana_hai')
    
    #Establishing Relationship by below line
    creator=relationship("User",back_populates="blogs")  # in relationship("Which table we are relating with uss table ka classname,back_populates="jaise yha creator naam se hai wha yhi relationship kis naam se hai")
    
    
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    #Reverse relation bana rhe 
    blogs=relationship("Blog",back_populates="creator")
    
    
