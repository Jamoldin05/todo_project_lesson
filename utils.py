import bcrypt
from serialazie import UserRegister
from session import Session


session = Session()


def hash_password(raw_password : str):
    encoded_password = raw_password.encode('utf-8') 
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(encoded_password,salt).decode()


def match_password(raw_passowrd : str, encoded_password:str):
    raw_passowrd = raw_passowrd.encode()
    return bcrypt.checkpw(raw_passowrd,encoded_password.encode())


class Response:
    def __init__(self,message,status_code = 200):
        self.message = message
        self.status_code = status_code
        
    def __str__(self):
        return f'{self.message} =  {self.status_code}'
    
    
    
def validate_user(dto : UserRegister):
    assert dto.username , 'Username must be required'
    assert dto.password , 'Password must be required'
    
    
    
    
def login_required(func):
    def wrapper(*args,**kwargs):
        if not session.session:
            return Response('Login required',404)
        
        return func(*args,**kwargs)
    
    return wrapper



def is_admin(func):
    def wrapper(*args,**kwargs):
        if session.session.role != 'admin':
            return Response('Only admin user can be changed')
        
        return func(*args,**kwargs)
    return wrapper


