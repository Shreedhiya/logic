a=int(input("enter no:"))
b=int(input("enter no:"))
c=input("add/sub/div/mult")
if(c=="add"):
    print(a+b)
elif(c=="sub"):
    print(a-b)
elif(c=="mult"):
    print(a*b)
elif(c=="div"):
    print(a/b)
else:
    print("Invalid operation")
