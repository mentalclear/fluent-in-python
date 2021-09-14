a_list = [1, 2, 3]

b_list = a_list[:]

# alternatively
c_list = []
for i in a_list:
    b_list.append(i)

# compact version
d_list = [i for i in a_list]

print(f"\n{d_list}")

# A variation, operation done on list elements:

b_list = []
for i in a_list:
    b_list.append(i * i)

# The same can be acheived with list comps:

b_list = [i * i for i in a_list]

print(f"\n{b_list}")

# Here [ value  for_statement_header ]

# Example with 2 loops:
mult_last = []
for i in range(3):
    for j in range(3):
        mult_last.append(i * j)

print(f"\n{mult_last}")

# The same can be represented with list comp:

mult_last = [i * j for i in range(3) for j in range(3)]
print(f"\n{mult_last}")

# Another optional feature with if statements:
# [ value  for_statement_header  if_expression ]

my_list = [10, -10, -1, 12, -500, 13, 15, -3]

new_list = []
for i in my_list:
    if i > 0:
        new_list.append(i)

# List comp version:
new_list = [i for i in my_list if i > 0]
print(f"\n{new_list}")

