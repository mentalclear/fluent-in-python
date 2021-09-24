# A tuple built from another is actually the same exact tuple
t1 = (1, 2, 3)
t2 = tuple(t1)
print(t2 is t1)

t3 = t1[:]
print(t3 is t1)

# The same behavior can be observed with instances of str, bytes, and frozenset
test1 = (1, 2, 3)
test3 = (1, 2, 3)
print(test3 is test1) # This gives true! In reality it's false!!!

# try the same thing in console

s1 = 'ABC'
s2 = 'ABC'
print(s2 is s1)

