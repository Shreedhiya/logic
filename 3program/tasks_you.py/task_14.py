# create a 10 number of passwords


import random,string
for i in range(10):
    x="".join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=10))
    print(x)