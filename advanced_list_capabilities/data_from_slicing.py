a_list = [1, 2, 5, 10, 20, 30]

b_list = a_list[1:3]
c_list = a_list[4:]

print(f"{b_list} and {c_list}")

d_list = a_list[-4:-1]        # Produces [5, 10, 20]
e_list = a_list[-1:]          # Produces [30]

print(f"{d_list} and {e_list}")

#Example:
a_list = [100, 200, 300, 400, 500, 600]
b_list = a_list[2:5:2]      # Produces [300, 500]

# Copy of the list reversed:

rev_list = a_list[::-1]

print(rev_list)