from session import Session
from utils import Response, match_password
from db import cur
from db import commit
from models import User
from utils import hash_password



session = Session()



@commit
def login(username : str, password : str):
    user = session.check_session()
    if user:
        return Response('You already logged in' , 404)
    
    get_user_by_username = '''select * from users where username = %s;'''
    cur.execute(get_user_by_username,(username,))
    
    user_data = cur.fetchone()
    if not user_data:
        return Response('User not found',404)
    
    
    user = User.from_tuple(user_data)
    
    
    if not match_password(password,user.password):
        return Response('Password wrong',404)
    
    session.add_session(user)
    return Response('You successfully logged in.')
    
    


    

@commit
def register(username: str, password: str, email: str):
    user = session.check_session()
    if user:
        return Response('You already logged in', 400)

    check_user_query = '''select * from users where username = %s;'''
    cur.execute(check_user_query, (username,))
    if cur.fetchone():
        return Response('Username already taken', 400)

    check_email_query = '''select * from users where email = %s;'''
    cur.execute(check_email_query, (email,))
    if cur.fetchone():
        return Response('Email already registered', 400)

  
    hashed_password = hash_password(password)

   
    insert_user_query = '''
        insert into users (username, password, email)
        values (%s, %s, %s)
        returning *;
    '''
    cur.execute(insert_user_query, (username, hashed_password, email))
    new_user_data = cur.fetchone()


    new_user = User.from_tuple(new_user_data)


    session.add_session(new_user)

    return Response('You successfully registered', 201)

    



@commit
def logout():
    user = session.check_session()
    if not user:
        return Response("You are not logged in", 400)

    session.remove_session()
    return Response("You have successfully logged out", 200)

    
    
