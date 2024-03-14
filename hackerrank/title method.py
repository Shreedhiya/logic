input_user=input("enter a para:").split()
for i in input_user:
    for j in i:
        if j.isupper():
            print(i)
   