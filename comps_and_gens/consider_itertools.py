import itertools

# Use of chain. To combine multiple iterators into a single sequential iterator
it = itertools.chain([1, 2, 3],[4,5,6])
print(list(it))

# Use of repeat. Output a single value forever, or use the second parameter 
# to specify a maximum number of times
it = itertools.repeat('hello', 3)
print(list(it))

# Use of cycle. Repeat an iterator’s items forever
it = itertools.cycle([1, 2])
result = [next(it) for _ in range (10)]
print(result)

# Use of tee
it1, it2, it3 = itertools.tee(['first', 'second'], 3)
print(list(it1))
print(list(it2))
print(list(it3))

# zip_longest 
keys = ['one', 'two', 'three']
values = [1, 2]

normal = list(zip(keys, values))
print('zip: ', normal)

it = itertools.zip_longest(keys, values, fillvalue='nope')
longest = list(it)
print('zip_longest:', longest)

# Filtering Items from an iterator

# islice
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_five = itertools.islice(values, 5)
print('First five: ', list(first_five))

middle_odds = itertools.islice(values, 2, 8, 2)
print('Middle odds:', list(middle_odds))

# takewhile
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.takewhile(less_than_seven, values)
print(list(it))

# dropwhile
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.dropwhile(less_than_seven, values)
print(list(it))

# filterfalse
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = lambda x: x % 2 == 0

filter_result = filter(evens, values)
print('Filter:      ', list(filter_result))

filter_false_result = itertools.filterfalse(evens, values)
print('Filter false:', list(filter_false_result))

# Producing combinations of items for iterators

# accumulate
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_reduce = itertools.accumulate(values)
print('Sum:   ', list(sum_reduce))

def sum_modulo_20(first, second):
    output = first + second
    return output % 20

modulo_reduce = itertools.accumulate(values, sum_modulo_20)
print('Modulo:', list(modulo_reduce))

# product
single = itertools.product([1, 2], repeat=2)
print('Single: ', list(single))

multiple = itertools.product([1, 2], ['a', 'b'])
print('Multiple:', list(multiple))

# permutations
it = itertools.permutations([1, 2, 3, 4], 2)
print(list(it))

# combinations
it = itertools.combinations([1, 2, 3, 4], 2)
print(list(it))

# combinations_with_replacement
it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
print(list(it))
