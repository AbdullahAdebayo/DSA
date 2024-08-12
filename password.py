# name ="Olaitan Abdullah"
# password = "HelloHabibi"

# if name == "Olaitan Abdullah" and password == "HelloHabibi":
#     print("Incorrect Details")
# else:
#     print("Login Successful")



users = {
    "Olaitan" : "Oloobasemi",
    "Sodiq" : "Panther_Ysl",
    "Dapo" : "Tesla.py",
    "Moyo" : "RahimMoyo"
}

def login_details():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login Successful")
    else: 
        print("Incorrect login details")

login_details()        


# name = "Olaitan Abdullah"
# print(name)