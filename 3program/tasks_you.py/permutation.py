#print the combination of a b c
#not to print the repeated letters
#using permutation package

from itertools import permutations
letters=['a','b','c']
for i in permutations(letters):
    print("".join(i))