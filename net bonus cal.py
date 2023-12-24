salary=int(input("enter the employee salary:"))
service=int(input("enter the employee year of service:"))
bonus=(5/100)*salary
if(service>5):
    print("the net bonus is=",bonus)
else:
    print("no bonus")
