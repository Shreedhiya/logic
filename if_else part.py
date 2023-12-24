result=[]
mark=input("enter the marks:").split(",")
for x in mark:
    if int(x)>=35:
        result.append("pass")
    else:
        result.append("fail")
print(result)
