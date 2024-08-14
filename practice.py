import json

def signup():
    print("To signup")
    print("--"*25)
    username = input("Enter the username\nNOTE: use '_' instead of space:\t")
    password = input("Enter the password:\nNOTE: use '_' instead of space:\t")
    try:
        mobile_num = int(input("Enter your mobile number:\t"))
        if len(str(mobile_num)) != 10:
            raise ValueError
    except ValueError:
        print("Try to Enter the correct phone number")



    signup_dict = {
        "username" : username,
        "password" : password,
        "mobile_number" : mobile_num
    }

    try:
        with open("database.json","r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data= {}
        

    data_list = data["student"]
    data_list.append(signup_dict)
    data.update({"student" : data_list})

    with open("database.json",'w') as f:
        json.dump(data,f)
        print("Sign up successful")

def signin():
    print("To sign in")
    print("--"*25)
    username = input("Enter your username\t")
    password = input("Enter your password\t")
    with open("database.json",'r') as f:
        data = json.load(f)
    
    data_list = data["student"]
    for i in data_list:
        if (i["username"] == username):
            if (i["password"] == password):
                print("Logged in successfully")
                print(f"your phone number is {i["mobile_number"]}")
                return
            print("Incorrect Password")
            return

    print("No such username\n")


def credentials():
    print("1.Sign up\n2.Sign in\n")
    ch = int(input("ENter a choice"))
     
    if ch == 1:
        signup()    
    elif ch == 2:
        signin()
    else:
        print("choose either '1' or '2'")

while True:
    try:
        credentials()

    except:
        print("incorrect value")
    
    finally:
        ch = input("do you want to continue? (y/n)")
        if ch.lower() == 'y':
            pass

        elif ch.lower() == 'n':
            break

        else:
            print("Incorrect choice")
            print("Exiting program")
            break
