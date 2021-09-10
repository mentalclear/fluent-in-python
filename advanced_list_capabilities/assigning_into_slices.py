
my_list = [10, 20, 30, 40, 50, 60]
my_list[1:4] = [707, 777]

# This example has the effect of deleting the range [20, 30, 40]
# and inserting the list [707, 777] in its place. The resulting list is:
print(my_list)

# You may even assign into a position of length 0. 
# The effect is to insert new list items without deleting existing ones.

my_list = [1, 2, 3, 4]
my_list[0:0] = [-50, -40]
print(my_list)