# print current time and  print suitable sentence




import datetime
present_time=datetime.datetime.now().hour
if 5 <= present_time < 12:
    print("good morning")
elif 12 <= present_time  < 16:
    print("good afternoon")
elif 16 <= present_time < 21:
    print("good evening")
else:
    print("good night")
