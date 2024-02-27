import re
try:
    
    your_email_id =input("enter the email id:")
    find=re.search(r"@gmail.com",your_email_id)
    if find:
        print("your mail id  is valid ")
    else:
        print("your mail id is incorrect")


except Exception:
    print("something is wrong please try again")
