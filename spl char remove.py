the_string=input("enter a string:")
special_characters=['@','%','*']
for i in special_characters:
    the_string=the_string.replace(i,"")
print(the_string)
