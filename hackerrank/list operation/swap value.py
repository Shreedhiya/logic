# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	size = len(newList)
	
	# Swapping 
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	
	return newList
	
# Driver code
newList = [11, 35, 9, 56, 2]

print(swapList(newList))
# without function method
new_list=[10,20,30,40,50,60]
size=len(new_list)
temp=new_list[0]
new_list[0]=new_list[size-1]
new_list[size-1]=temp
print(new_list)
#another simple swap method
newList=[10,20,30]
newList[0], newList[-1] = newList[-1], newList[0]
print(newList)

# swap value in list 
list = [23, 65, 19, 90]
pos1, pos2  = 1, 3
list[pos1], list[pos2] = list[pos2], list[pos1]
print(list)


