#list.count(value)                 # Get no. of
#                                   #  instances.
# list.index(value[, beg [, end]])  # Get index of value.
# list.pop([index])                 # Return and remove
#                                   #  indexed item:
#                                   #  last by default.

yr_list = [1, 2, 1, 1,[3, 4]]
print(yr_list.count(1))       # Prints 3
print(yr_list.count(2))       # Prints 1

# It returns the number of matching items at the top level only. So 0
print(yr_list.count(3))       # Prints 0
print(yr_list.count([3, 4]))  # Prints 1
print("\n")
beat_list = ['John', 'Paul', 'George', 'Ringo']
print(beat_list.index('Ringo'))   # Print 3.



