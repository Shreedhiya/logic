#get the list of numbers as a input
# return the maximum  and minimum values 
#map is used to iterates up on all the specified elements without the usage of any loops.



numbers=list(map(int,input("enter the numbers:").split()))
print("maximumnumbers:",max(numbers))
print("mininumbers",min(numbers))