import abc

class BasePizza(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_ingredients(self):
        """Returns the ingredient list"""
    
class Calzone(BasePizza):
    def get_ingredients(self, with_egg=False):
        egg = Egg() if with_egg else None
        return self.ingredients + [egg]

# static method in the subclass
class DietPizza(BasePizza):
    @staticmethod
    def get_ingredients():
        return None

# It's possible to use @staticmethod and @classmethod decorators
# on top of the abstract method

class BasePizzaNew(object, metaclass=abc.ABCMeta):
    ingredients = ['cheese']
    @classmethod
    @abc.abstractmethod
    def get_igredients(cls):
        """Returns the ingredients list"""
        return cls.ingredients

        
        