number=int(input("enter a number of students:"))
name=[]
mark=[]
for x in range(number):
    n,m=input("enter a student name&marks :").split()
    name.append(n)
    mark.append(m)
max(mark)
mark.index(max(mark))
print(name[mark.index(max(mark))],"is highest mark")
