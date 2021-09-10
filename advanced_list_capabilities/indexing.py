my_list = [100, 500, 1000]
print(my_list[0])

my_list[1] = 55 
print(my_list)


a_list = [100, 200, 300, 400, 500, 600]

# a_list[6]  # yelds index error

# Performance tip - use one line print statments for multiple vars
# when it's reasonable

# Negative indexing starts from the right
print(a_list[-2]) # returns 500

# Generating Index Numbers Using “enumerate”

# The “Pythonic” way is to avoid the range function 
# except where it’s needed.

a_list = ['Tom', 'Dick', 'Jane']

for s in a_list:
    print(s)

# The above approach is more natural and efficient than relying 
# on indexing, which would be inefficient and slower.

for i in range(len(a_list)):
    print(a_list[i])

# Using enumerate function
print(list(enumerate(a_list,1))) # Index starts with 1, can be ommited and becomes 0

for item_num, name_str in enumerate(a_list,1):
    print(f"{item_num}. {name_str}")

