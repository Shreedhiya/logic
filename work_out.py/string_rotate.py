import re
try:
    input_str=input("Enter a para: ").split()
    for i in input_str:
        print(i)
        camel_case=re.findall("[a-z]+[A-Z]*",i)
        print(" ".join(),camel_case)

except Exception:
    print("invalid")




