from passlib.context import CryptContext  #This is for hashing our passwords


pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")


class Hash():
    def bcrypt(password:str):
           hashed_pswd=pwd_cxt.hash(password[:72])  #[:72] is used to truncate the password to 72 bytes , nhi toh error aa rha tha
           return hashed_pswd
       
    def verify(request_password,hashed_password):
        return pwd_cxt.verify(request_password,hashed_password)
    #request password is our plain password which we recieve from user through request schema on our frontEnd
        