import re
try:
    sentence=" zero is a number"
    match=re.findall(r'\b\w*z\w*\b',sentence)
    print(match)

except Exception:
    print("something is wrong please try again")