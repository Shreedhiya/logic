#evaluate the multiple operation in same line
# eval is a build in function that allows us to evaluate the python expression as a 'string' and return the value as an integer.


a=input("enter a mathematical expression:")
result=eval(a)
print(f"result:{result}")