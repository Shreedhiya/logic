
import re  0

file_heandling=open("data_file.txt","a")
file_heandling_read=open("data_file.txt","r")

print("1 press login page")
print("2 press regester page")

key=int(input("Enter :"))

data_file_store=[]
for i in file_heandling_read:
        data_file_store.append(i.split(","))
# login table
if key==1:
    user_name=input("enter Name:")
    password=input("enter password:")
    email=input("Enter email id:")
    number=input("Enter your mobile number:")

def is_strong_password(password):
    if len(password)<8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any (char.islower() for char in password):
        return False
    return True

user_password=input("enter a password:")



for j in data_file_store:
    if user_name==j[0]:
        if password==j[1]:
            print("\n    Successfull ")
        else:
            print("\n    Password is Not matched\n")
        if email==j[2]:
            print("your mail id  is valid ")
        else:
            print("your mail id is incorrect")
        if number==j[3]:
            if len(number)==10:
                print("number is valid")
            else:
                print("number is invalid")

#crate table
if key==2:
    create_user_name=input("Enter your name :")
    create_password=input("Create your password  :")

    return_password=input("Return your passsword :")
    create_email=input("enter your id:",re.search(r"@gmail.com"))
    create_number=int(input("enter valid number:"))
else:
    print("please register correctly")
      

    
 