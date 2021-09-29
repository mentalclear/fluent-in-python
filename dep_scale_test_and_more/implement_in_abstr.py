import abc

class BasePizza(object, metaclass=abc.ABCMeta):
    default_ingredients = ['cheese']
    @classmethod
    @abc.abstractmethod
    def get_igredients(cls):
        """Returns the ingredients list"""
        return cls.default_ingredients

# You can put code in your abstract methods and call it using super()
class DietPizza(BasePizza):
    def get_ingredients(self):
        return [Egg()] + super(DietPizza, self).get_igredients()