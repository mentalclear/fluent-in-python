# Decorator
def identity(f):
    return f

# The usage:
@identity
def foo():
    return 'bar'


# the register decorator stores the decorated function name into a dictionary. 
# The _functions dictionary can then be used and accessed using the 
# function name to retrieve a function: _functions['foo'] points 
# to the foo() function.
_functions = {}
def register(f):
    global _functions
    _functions[f.__name__] = f
    return f

@register
def foo():
    return 'bar'
