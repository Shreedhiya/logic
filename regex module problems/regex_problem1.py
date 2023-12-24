'''Write a program that matches a string that has an N followed by zero or more o's'''

import re
a=input("enter the string:")
match=re.findall("^no*$",a)
if match:
    print("matched")
else:
    print("not matched")