string=input("Enter any string:")
def vowels(string):
    for char in string:
        if char in "aeiouAEIOU":
            print(char,end=" ")
    return char
vowels(string)
