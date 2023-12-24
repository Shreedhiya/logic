n=int(input("enter a number"))
even_count=0
odd_count=0
for number in range(n):
    if number % 2 == 0:
        even_count+=1
    else:
        odd_count+=1

print("even number", even_count)
print("odd number", odd_count)
