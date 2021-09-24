# del is not a function, it's a statement
# we write del x and not del(x)

# del deletes references
a = [1, 2]
b = a
print(f"b: {id(b)} a: {id(a)}")
del a  # reference a removed but b is still pointing there
print(f"b: {id(b)}")
print(b)  

b = [3] # no old object can be discarded
print(f"b: {id(b)}")