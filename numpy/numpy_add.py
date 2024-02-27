

import numpy as np
num1=np.array([[1,2,3],[3,4,5],[4,6,7]])
num2=np.array([[3,5,6],[7,8,9],[7,0,2]])
num=np.concatenate([num1,num2],axis=1)     # column accessing axis=1
print(num)

# stack method   # we cannot using axis in stack method
harizontal_stack=np.hstack([num1,num2])
print(harizontal_stack)

vertical_stack=np.vstack([num1,num2])
print(vertical_stack)

num_stack=np.dstack([num1,num2])  #1*1 2*2 3*3
print(num_stack)

#split method

nums_hsplit=np.hsplit(num1,2)
print(nums_hsplit)

nums_vsplit=np.vsplit(num1,3)
print(nums_vsplit)

nums=np.dsplit(num1,3)   #spliting arrays
print(nums)



