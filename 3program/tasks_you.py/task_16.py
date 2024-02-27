# evaluate the current age,counts of days and months from birth 



from datetime import date
dob=date(2004,12,19)
today=date.today()
time_diff=today-dob
d=time_diff.days
m=int((d/365)*12)
y=int(d/365) 
print(f"years: {y}")
print(f"months: {m}")
print(f"days: {d}")


