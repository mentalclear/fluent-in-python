class HauntedBus:
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=[]):  
        self.passengers = passengers  

    def pick(self, name):
        self.passengers.append(name)  

    def drop(self, name):
        self.passengers.remove(name)


# Behavior of the bus like that:
#

bus1 = HauntedBus(['Alice', 'Bill'])  
print(bus1.passengers)
#['Alice', 'Bill']
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)  
#['Bill', 'Charlie']
bus2 = HauntedBus()  
bus2.pick('Carrie')
print(bus2.passengers)
#['Carrie']
bus3 = HauntedBus()  
print(bus3.passengers)  # The default empty list is no longer empty!
# ['Carrie']
bus3.pick('Dave')
print(bus2.passengers)   # Dave was picked up by bus 3 but appears in bus2
#['Carrie', 'Dave']
print(bus2.passengers is bus3.passengers)  
# The problem: bus2.passengers and bus3.passengers refer to the same list.
#True
print(bus1.passengers)
#['Bill', 'Charlie']        