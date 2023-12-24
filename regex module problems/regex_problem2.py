'''wrtie a program that matches a string that has an N followed by one or more o's.'''

import re

a=input("Enter The String:")
match=re.findall("^n.+",a)
if match:
    print("Matched")
else:
    print("not matched")