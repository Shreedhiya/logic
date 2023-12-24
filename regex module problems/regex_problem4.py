#Write a program that matches a word at the beginning of a string

import re
a=input("Enter The String:")
match=re.findall("^\w",a)

if match:
    print("Matched")
else:
    print("Not match")