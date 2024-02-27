#get a paragraph as a input and return the count replace words


a=input("enter a paragraph:")
b=input("enter a word u want to remove:")
c=input("enter a word u want to replace:")
count=a.split().count(b)
d=a.replace(b,c)
print("replaced paragraph:",d)
print("replaced word count",count)