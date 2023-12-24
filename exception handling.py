print("Hii")
try:
    a = int(input())
    b = int(input())
    c=a/b
    print(c)
except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("your input is wrong")

print("Bye")
