#The code in parentheses is a Python expression that returns 
# the list of class objects to be used as the class’s parents. 
# Ordinarily, you would specify them directly, but you could 
# also write something like this to specify the list of parent objects:

def parent():
    return object

class A(parent()):
    pass

print(A.mro())

# The class method mro() returns the method resolution order used 
# to resolve attributes—it defines how the next method to call 
# is found via the tree of inheritance between classes. 

class A1(object):
    bar = 42
    def foo(self):
        pass

class B1(object):
    bar = 0

class C1(A1, B1):
    xyz = 'abc'

print(C1.mro())

print(super(C1, C1()).bar)
print(super(C1, C1()).foo)
print(super(B1).__self__)
print(super(B1, B1()).__self__)

# Since no second argument provided super object cannot be bound to any instance.
print(super(C1))

#print(super(C1).foo)
#print(super(C1).bar)
#print(super(C1).xyz)

# Will complain that none of these attributes are available for the object like that

# At first glance, it might seem like this unbound kind of super 
# object is useless, but actually the way the super class implements 
# the descriptor protocol __get__ makes unbound super objects useful 
# as class attributes:
class D1(C1):
    sup = super(C1)

print(D1().sup)
print(D1().sup.foo)
print(D1().sup.bar)