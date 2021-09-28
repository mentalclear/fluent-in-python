class Pizza(object):
    @staticmethod
    def get_radius():
        raise NotImplementedError

print(Pizza())
#print(Pizza().get_radius()) # Raises not implemented


import abc

class BasePizza(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_radius(self):
        """Method that should do something"""

# Produces: TypeError: Can't instantiate abstract class 
# BasePizza with abstract method get_radius
BasePizza()         

