
def letter(string):
    try:
        index=0
        output=[]

        for i in range(1,len(string)+1):
            output.append(i*string[index])
            index+=1
        print("-".join(output).title())   
    except Exception as e:
        print("error:",e)
input_string=input("enter the string :")
letter(input_string)

#2
def leter(str):
    try:
        output=""                               #declare empty string
        for j in range(len(str)):               #iterate length of str
            output+=str[j].upper()+str[j]*j+'-' #fist leter is upper use upper() #str[j] mean str[0] value is m like all                                     
        print(output)                           #print output
    except Exception as e:
        print(e)         
str=input("enter a string")
leter(str)              
#if alter use zip() 
"""
for i,j in zip(str,range(len(str))):
    output+=i.upper()+i*j+'-'
print(output)
"""

