# Passed to the function value will not change after the 
# funciton execution is completed.
def double_it(n):
    n * 2
    print (n)
test = 2
double_it(test)
print(test)

# With list the behavior is different, the change will be applied:
def set_list_vals(list_arg):
    list_arg[0] = 100
    list_arg[1] = 200
    list_arg[2] = 150
a_list = [0, 0, 0]
set_list_vals(a_list)
print(a_list)          # Prints [100, 200, 150]

# Another example where values will not change:
def set_list_vals(list_arg):
    list_arg = [100, 200, 150]

a_list = [0, 0, 0]
set_list_vals(a_list)
print(a_list)          # Prints [0, 0, 0]

# Here list_arg was reassigned to refer to a completely new list. 
# The association between the variable list_arg and the original data, 
# [0, 0, 0]), was broken.
# slicing and indexing are different. Assigning into an indexed item or a slice 
# of a list does not change what the name refers to; it still refers to 
# the same list, but the first element of that list is modified.
