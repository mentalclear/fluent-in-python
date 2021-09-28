class Pizza(object):
    def __init__(self, size):
        self.size = size
    
    def get_size(self):
        return self.size

print(Pizza.get_size) # Returns function object

# Direct call with no object gives an error 
# Pizza.get_size()

# This will work for example
print(
    Pizza.get_size(Pizza(42))
    )

# Binding class methods to its instances
print(Pizza(42).get_size)
print(Pizza(42).get_size())

# Another example 
m = Pizza(42).get_size
print(m())

# As long as you have a reference to the bound method, you do not even 
# have to keep a reference to your Pizza object.
# if you have a reference to a method but you want to find out which object 
# it is bound to, you can just check the method’s __self__ property, like so:
print(m.__self__)
print(m == m.__self__.get_size)
