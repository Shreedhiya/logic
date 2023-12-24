input_string=input("Enter a string:")
words=input_string.split()
reversed_words=[word[::-1] for word in words]
output_string=' '.join(reversed_words)
print(output_string)
