# Now the complete class doing that:
class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  
        else:
            #self.passengers = passengers  # this is a bug!
            self.passengers = list(passengers) # Fixed! Makes a copy of the list.

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

# self.passengers = passengers this assignment makes 
# an alias for the passangers list
# so the methods later are actually mutating the original list.

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)
print(bus.passengers)

# In this example the basketball team drops 2 members because
# they were dropped by the bus.

# TwilightBus violates the "Principe lo least astonishment"(least surprise)


