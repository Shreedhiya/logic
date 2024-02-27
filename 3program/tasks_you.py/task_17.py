# counting the numbers at the end  to print the statement

#sleep(x)  x is represent to the seconds
import time
i=10
while(0<=i):
    time.sleep(1)   # number of seconds for which the code is required to be stopped 
    print(i)
    i-=1
if i<0:
    print("happy coding")  