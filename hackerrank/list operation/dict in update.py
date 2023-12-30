dict1={1:1,3:3,5:5}
dict2={3:5,9:6,0:5}
dict3={6:0,8:4,9:6}
dict4={}
for d in (dict1,dict2,dict3):
    dict4.update(d)
print(dict4)

#another method to add the values in one column
try:

    n=int(input("enter the number:"))
    d=dict()
    for x in range(1,n+1):
        d[x]=x*x

    print(d)

except Exception:
    print("invalid input or error occured")
