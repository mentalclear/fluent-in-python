# Using a static method mix_ingerdients
class Pizza(object):
    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)


# Bound methods are objects, too, and creating them has a CPU and 
# memory cost—even if it’s low.

print(Pizza().cook is Pizza().cook)
print(Pizza().mix_ingredients is Pizza.mix_ingredients)
print(Pizza().mix_ingredients is Pizza().mix_ingredients)

# Second, static methods improve the readability of the code. 
# When we see @staticmethod, we know that the method 
# does not depend on the state of the object.

# Third, static methods can be overridden in subclasses. 