# get a input in random 10 numbers 
# set output as if random is equally in user_input 
# random defines a series of functions for generating or manipulating random integers
# randint() - returns a random number between the given range 

import random
user_input=int(input("enter the number:"))
read_int=random.randint(1,11)
if user_input==read_int:
    print("you win")
else:
    print("try again")