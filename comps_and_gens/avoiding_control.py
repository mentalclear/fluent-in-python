matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

squared = [[x**2 for x in row] for row in matrix]
print(squared)

my_lists = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]] ]
flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]


flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)

print(flat)

# List comps have an implicit and expression
# these to are equivalent
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]

# I want to filter a matrix so the only cells remaining are those 
# divisible by 3 in rows that sum to 10 or higher. 

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(filtered)

# The rule of thumb is to avoid using more than two control 
# subexpressions in a comprehension. 