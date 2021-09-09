from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb') 
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)

# As you can see, array.tofile and array.fromfile are easy to use. 
# If you try the example, you’ll notice they are also very fast. 
# A quick experiment shows that it takes about 0.1s for array.fromfile 
# to load 10 million double-precision floats from a binary file 
# created with array.tofile. 