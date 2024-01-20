try:
    date= "12-11-2011"
    result=date.split("-")
    changed_date=[ i for i in reversed(result)]
    print("-".join(changed_date))
 
except Exception:
    print("something is wrong please try again")
