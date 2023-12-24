n=int(input("Enter a number:"))

for i in range(1, n+1):

    for j in range(n, i, -1):
        print(" ", end="")

    for j in range(1, i):
        print(chr(64+j), end="")

    print(chr(64+i), end="")

    for  j in range(i-1, 0, -1):
        print(chr(64+j), end="")

    print()
