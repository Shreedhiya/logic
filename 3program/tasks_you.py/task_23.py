


import string
import time
start_time=time.time()
for letter in string.ascii_letters:
    input_letter=input("enter a letter:")
    if input_letter!=letter:
        print("sorry,game over")
        exit()
    end_time=time.time()
    elapse_time=round(end_time-start_time,3)
    print("you have completed in"+str(elapse_time)+"seconds")