# this demoes the assigning a new list variable(reference)
a_list = [2, 5, 10]
b_list = a_list

print(f"\n{a_list} and {b_list}")

b_list.remove(5)
print(f"\n{a_list} and {b_list}")

# To actually copy:
my_list = [1, 10, 5]
your_list = my_list[:] 

your_list.append(100)
print(f"\n{my_list} and {your_list}")


