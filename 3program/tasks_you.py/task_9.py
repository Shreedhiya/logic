# times schedule for all period get input 
# and set output for hour based period


try:



    def period(hour):

        if  9<= hour <10:
            return "tamil period"
        elif 10<= hour <11:
            return "english period"
        elif 11<= hour <=12:
            return "maths period"
        elif 12<= hour <1:
            return "lunch break"
        elif 1<=hour <2:
            return "science period"
        elif 2<= hour <3:
            return "social period"
        else:
            return "its time to go home"
        
    hour=int(input("enter the time:"))
    period=period(hour)
    print("the period is ",period)

except Exception:
    print("invaild code ")

  
   

    















