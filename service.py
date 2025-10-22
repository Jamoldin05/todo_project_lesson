from session import Session
from utils import Response, match_password,validate_user, hash_password,login_required,is_admin
from db import cur, commit
from models import User, UserRole, TodoType
from serialazie import UserRegister



session = Session()




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
def register(username : str | None = None, password : str | None = None,email : str | None = None):
    dto = UserRegister(username,password)
    validate_user(dto)
    get_user_by_username = '''select * from users where username = %s;'''
    cur.execute(get_user_by_username,(username,))
    user_data = cur.fetchone()
    if user_data:
        return Response(message='User already exists',status_code=404)
    
    insert_user_query = '''insert into users(username,password,email,role)
        values (%s,%s,%s,%s);
    '''
    
    data = (dto.username,hash_password(dto.password),email, UserRole.USER.value)
    cur.execute(insert_user_query,data)
    return Response('User created',201)



def logout():
    if session.session:
        session.session = None
        return Response('You logged out !',204)
    
    return Response('You must be login.',404)




@login_required
@is_admin
@commit
def add_todo(title : str, description : str | None = None ):
    
    user = session.session
    
    insert_todo_query = '''insert into todos(title,user_id,todo_type)
        values(%s,%s,%s);
    '''
    
    cur.execute(insert_todo_query,(title,user.id,TodoType.PERSONAL.value ))
    return Response('Todo inserted',201)


        
@login_required
@is_admin
@commit
def update_admin_role(user_id):
    all_users_query = '''select * from users where role = 'user' ;'''
    cur.execute(all_users_query)
    users = cur.fetchall()
    for user in users:
        print(user)
        
    update_user_role_query = '''update users set role = 'admin' where id = %s; '''
    cur.execute(update_user_role_query,(user_id,))
    return Response('User updated',202)
    
        
    
        
 
def get_user_todos():
    pass


    
    
    