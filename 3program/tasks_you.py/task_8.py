# input the all domains and ask user to select the domain and print it
try:
    domain=["data analysists","python developer","cyber security","software developer"]
    user_domain=input("select your domain:")
    for i in domain:
        if i==user_domain:
            print(i)
    else:
        print("domain is not found")

except Exception:
    print("invalid code please check again!")

