import json

def stored_user():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user():
    username = input("Please enter your name :")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj) #存储user name
    return username

def greet_user():
    current_user = input("Let us know your name: ")
    username = stored_user()
    if username == current_user:
        print('Welcome back ' + username + '!')
    else:
        print("This is your first time !")
        username = get_new_user()
        print("We will remember your name next time " + username + '!')

greet_user()