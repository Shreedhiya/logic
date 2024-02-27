# universal function for rounding decimals using numpy

import numpy as np
trunc=np.trunc([-2.445,3.8674])   # trunc is used to returns truncated value 
around=np.around([-2.845,6.789])   # round an array of floats to a given number of decimals
floor=np.floor([-2.845,9.345])    # this is same as round method
ceil=np.ceil([-2.789,-5.678])     # rounds a number nearest integer vary in positive and negative numbers
print(trunc)
print(around)
print(floor)
print(ceil)

