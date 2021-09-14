# Set comprehansion 

a_list = [5, 5, 5, -20, 2, -1, 2]
my_set = set( )
for i in a_list:
    if i > 0:
        my_set.add(i)

# The same can be done with set comp:

my_set = {i for i in a_list if i > 0}        

print(f"\n{my_set}")

my_squared_set = {i * i  for i in a_list if i > 0}

print(f"\n{my_squared_set}")


# Dictionary Comprehensions

vals_list = [('pi', 3.14), ('phi', 1.618)]

my_dict = {i[0]:i[1] for i in vals_list}

print(f"\n{my_dict}")
print(f"\n{my_dict['pi']}")

# if there are two lists of the same size they can be put 
# in a dictionary using the same dict comp:
keys = ['Bob', 'Carol', 'Ted', 'Alice' ]
vals = [4.0, 4.0, 3.75, 3.9]
grade_dict= { keys[i]: vals[i] for i in range(len(keys)) }
print(f"\n{grade_dict}")

# Perfromance tip:
grade_dict = { key: val for key, val in zip(keys, vals)}

# Example, inversion of the list, for a phone book for exmaple:
phone_dict = {"Jay": 5713995658, "Alex": 5714587451}
idict = {v : k for k, v in phone_dict.items() }
print(f"\n{phone_dict}")
print(f"\n{idict}")