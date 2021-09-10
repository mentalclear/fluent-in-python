# naming for variables including list and type
my_int_list = [5, -20, 5, 69]

beat_list = [ 'John', 'Paul', 'George', 'Ringo' ]

mixed_list = [10, 'John', 5, 'Paul' ]

# But you should mostly avoid mixing data types inside lists. 
# In Python 3.0, mixing data types prevents you from using 
# the sort method on the list. 
# ints and floating points are ok, though

num_list = [3, 2, 17, 2.5]
num_list.sort()  # Sorts into [2, 2.5, 3, 17]
print(num_list)

# declaring a list and then append to it

my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(f"\n{my_list}")

# then remove 

my_list.remove(1)
print(f"\n{my_list}")

# Example three different judges all assigned the score 1.0, 
# but the third judge assigned 9.8.

the_scores = [1.0, 1.0, 9.8, 1.0]

# remove will remove only the first instace from the left
the_scores.remove(1.0)

print(the_scores)
