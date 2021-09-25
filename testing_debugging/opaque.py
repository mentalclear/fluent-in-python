# For instances of Python classes, 
# the default human-readable string value is the same as the repr value.

class OpaqueClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = OpaqueClass(1, 'foo')
print(obj)

# This output can’t be passed to the eval function, and it says nothing 
# about the instance fields of the object.

# print(obj.x)
# print(obj.y)

# There are two solutions to this problem. If you have control of the class, 
# you can define your own __repr__ special method that returns 
# a string containing the Python expression that re-creates the object. 

class BetterClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def __repr__(self):
        return f'BetterClass({self.x!r}, {self.y!r})'

obj = BetterClass(1, 'bar')
print(obj)

# When there's no access to the class:
obj = OpaqueClass(4, 'foo')
print(obj.__dict__) # this is really cool actually.
