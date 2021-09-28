class Pizza(object):
    radius = 42
    @classmethod
    def get_radius(cls):
        return cls.radius

print(Pizza.get_radius)
print(Pizza().get_radius)
print(Pizza.get_radius is Pizza().get_radius) 
# True in the book. But for me returns False.





