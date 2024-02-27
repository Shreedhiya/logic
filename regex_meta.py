#sequence of character form of search pattern 

import re
a="this is a string."
match=re.search(".$",a) #it matches the end of the string
print(match)
match=re.findall(".",a) #it matches the only single character except the new line
print(match)
match=re.search("^th",a) # it matches the beginning string
print(match)
match=re.findall("[a-z]",a) #it identify the alphabets
print(match)
match=re.search("s|a",a) #if any one of the character is present it will match 
print(match)
match=re.findall("[abc]",a) # it contain sequence of character
print(match)
match=re.search("is?i",a) #present zero or one time
print(match)
match=re.search("is",a)  
print(match)
match=re.findall("\.",a)  #it is not treated in special way 
print(match)
match=re.findall("a*",a)  #present one or more time (include the empty space)
print(match)
match =re.findall("a+",a)   #should present one or more time
print(match)
match=re.search("a{2,3}",a) # {m,n} m-no.of time n 
print(match)
c="acd"
match=re.search("(a|b)cd",c)  #group the sub-pattern
print(match)
