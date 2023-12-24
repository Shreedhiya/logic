#write a program that matches a number at the end of a string.

import re
string=input("Enter the string and ending in digit:")
match=re.findall("\d$",string)

if match:
    print("Matched")
else:
    print("Not Matched")