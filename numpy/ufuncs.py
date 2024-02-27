# arithmetic methods solve using numpy


import numpy as np
x=np.array([1,-2,3,4,5])
y=np.array([5,6,7,8,9])
z=np.add(x,y)       # add method is used to add the values of 2 arrays
s=np.subtract(x,y)   #subtract method is used to subtract the 2 array values
m=np.multiply(x,y)    # multiply method is used to multiply the 2 array values
d=np.divide(x,y)      # divide method is used to dived the 2 array values
p=np.power(x,y)     #power method is used to raise the elements of an array to a specified power
r=np.remainder(x,y)   # remainder or mod() is used to return the remainder values
dv=np.divmod(x,y)     # divmod is used to return the quotient and remainder values
a=np.absolute(x)      # absolute method is used to convert all the negative values into positive values
print(z)
print(s)
print(m)
print(d)
print(p)
print(r)
print(dv)
print(a)