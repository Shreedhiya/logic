string=input("enter a string").split()
for i in string[1]:
    if i not in string[0]:
        print(i,end="")
    
 