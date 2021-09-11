a_list = [1, 2, [5, 10]]
b_list = a_list[:]          # Member-by-member copy.


print(f"{a_list} and {b_list}")
# Now, let’s modify b_list through indexing, setting each element to 0:

b_list[0] = 0
b_list[1] = 0
b_list[2][0] = 0
b_list[2][1] = 0

print(f"\n{a_list}")  # [1, 2, [0, 0]]

# The member-by-member copy, carried out earlier, copied the values 1 and 2, 
# followed by a reference to the list-within-a-list. Consequently, 
# changes made to b_list can affect a_list if they involve the second level.

### Shallow copying makes new copies of top-level data only.

# Deep copy for lists:
import copy

a_list = [1, 2, [5, 10]]
b_list = copy.deepcopy(a_list)

print(f"\na_list: {a_list}")
print(f"\nb_list: {b_list}")

# With deep copying, the depth of copying extends to every level. 
# You could have collections within collections to any level of complexity.

