from service import login,register,logout,add_todo,update_admin_role
import logging
from crud import create_task, get_all_tasks, update_task, delete_task
import os

def login_page():
    username = input('Username : ')
    password = input('Password : ')
    response = login(username,password)
    print(response)
    
    

def register_page():
    username = input('Username : ')
    password = input('Password : ')
    email = input('Email : ')
    response = register(username,password,email)
    print(response)


def logout_page():
    response = logout()
    print(response)
    

def add_todo_page():
    title = input('Title : ')
    description = input('Description : ')
    response = add_todo(title,description)
    print(response)
    

def update_role_page():
    user_id = int(input('USER ID: '))
    response = update_admin_role(user_id)
    print(response)



def menu():
    print("""
          Login => 1
          Register => 2
          Logout => 3
          Todo Add => 4
          Update Role => 5
          Exit => q 
          """)
    return input("?:")

def run():
    while True:
        choice = menu()
        if choice == '1':
            login_page()
            
        elif choice == '2':
            register_page()
            
        elif choice == '3':
            logout_page()
            
        elif choice == '4':
            add_todo_page()
            
        elif choice == '5':
            update_role_page()
            
            
            
        elif choice == 'q':
            break
            
        else:
            print('Invalid choice')
            continue
            
            
            
            
if __name__ == '__main__':
    run()



os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",     
    level=logging.INFO,          
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"                 
)

def main():
    logging.info("Todo Project ishga tushdi")

    create_task("Python loyihasini tugatish")
    create_task("PostgreSQL ulanishni sozlash")
    update_task(0, "Python loyihasini yakunlash")
    delete_task(1)

    print(get_all_tasks())

    logging.info("Todo Project yakunlandi")

if __name__ == "__main__":
    main()
