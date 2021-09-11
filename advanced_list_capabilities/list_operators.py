a_list = [1, 3, 5, 0, 2]
b_list = a_list      # Make an alias.
c_list = a_list[:]   # Member-by-member copy

# Initializing a large array
big_array = [0] * 1000
print(len(big_array))


a = [1, 2, 3]
print(None in a)  # This produces False
print([] in a)    # So does this.

b = [1, 2, 3, [], None]
print(None in b)                 # This produces True
print([] in b)                   # So does this.