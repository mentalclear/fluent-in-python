def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

# Surprisingly, calling normalize on the read_visits generator’s 
# return value produces no results:

it = read_visits('comps_and_gens/my_numbers.txt')
# percentages = normalize(it)
# print(percentages)
print(list(it))
print(list(it))  # Already exhausted

# So the problem here is the exhausted iterator

# Solution to the problem:
def normalize_copy(numbers):
    numbers_copy = list(numbers) # Copy the iterator
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result

it = read_visits('comps_and_gens/my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)
assert sum(percentages) == 100.0

# Still there is a problem. Copying an iterator can cause the memory problems later
# A way around this is to accept a function that returns a new iterator 
# each time it’s called
def normalize_func(get_iter):
    total = sum(get_iter()) # New iterator
    result = []
    for value in get_iter(): # New iterator
        percent = 100 * value / total
        result.append(percent)
    return result

# to use the above function a lambda expression can be used that calls the 
# generator and produces a new iterator each time
path = 'comps_and_gens/my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
assert sum(percentages) == 100

# A better way to achieve the same result is to provide 
# a new container class that implements the iterator protocol.

class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0

# Test an input value for this behavior and raise a TypeError to reject arguments 
# that can’t be repeatedly iterated over:
# def normalize_defensive(numbers):
#     if iter(numbers) is numbers: # An iterator -- bad!
#         raise TypeError('Must supply a container')
#     total = sum(numbers)
#     result = []
#     for value in numbers:
#         percent = 100 * value / total
#         result.append(percent)
#     return result

# Alternatively, the collections.abc built-in module defines an Iterator 
# class that can be used in an isinstance test to recognize the potential problem
from collections.abc import Iterator

def normalize_defensive(numbers):
    if isinstance(numbers, Iterator): # Another way to check
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize_defensive(visits)
assert sum(percentages) == 100.0

visits = ReadVisits(path)
percentages = normalize_defensive(visits)
assert sum(percentages) == 100.0

# The function raises an exception if the input is an iterator 
# rather than a container:
# visits = [15, 35, 80]
# it = iter(visits)
# normalize_defensive(it)

