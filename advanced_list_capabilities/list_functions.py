collection = [1, 2, 3, 4, 5]
len(collection)       # Return length of the collection
max(collection)       # Return the elem with maximum
                      #  value.
min(collection)       # Return the elem with minimum
                      #  value.
reversed(collection)  # Produce iter in reversed order.
sorted(collection)    # Produce list in sorted order.
sum(collection)       # Adds up all the elements, which
                      #  must be numeric.

a_list = [100, -3, -5, 120]
for i in range(len(a_list)):
    a_list[i] *= 2                      

print('Length of the list is', len(a_list))
print('Max and min are', max(a_list), min(a_list))

a_tup = (30, 55, 15, 45)
print(sorted(a_tup))    # Print [15, 30, 45, 55]

a_tup = (1, 3, 5, 0)
for i in reversed(a_tup):
    print(i, end=' ')

# Alternatively:
print(tuple(reversed(a_tup)))    