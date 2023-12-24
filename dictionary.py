students={"aarthi":89,"muthu":76,"viknesh":23,"ganesh":30}
duplicate_student={}
for key,value in students.items():
    if value>30:
        duplicate_student[key]=value
print(duplicate_student)
