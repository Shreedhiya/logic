#write a program that matches a string that has an O followed by two to three 'k'

import re

a=input("Enter The String:")
match=re.findall("ok?k",a)
if match:
    print("Matched")
else:
    print("Not matched")