from service import login


while True:
    choice = input('choice : ')
    if choice == '1':
        username = input('username : ')
        password = input('password : ')
        
        result = login(username,password)
        
        print(result)
    
    elif choice == 'q':
        break
    
    
    