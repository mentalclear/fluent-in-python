stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']

def get_batches(count, size):
    return count // size

result = {}
for name in order:
  count = stock.get(name, 0)
  batches = get_batches(count, 8)
  if batches:
    result[name] = batches
print(result)

# With dict comps:
found = {name: get_batches(stock.get(name, 0), 8)
         for name in order
         if get_batches(stock.get(name, 0), 8)}
print(found)

# Sync problme with (stock.get(name, 0), 8)
has_bug = {name: get_batches(stock.get(name, 0), 4)
           for name in order
           if get_batches(stock.get(name, 0), 8)}

print('Expected:', found)
print('Found: ', has_bug)

found = {name: batches for name in order
         if (batches := get_batches(stock.get(name, 0), 8))}

print(found)         

# reference the variable it defines in other parts of the comprehension
# will result in error:
# result = {name: (tenth := count // 10)
#           for name, count in stock.items() if tenth > 0}

# Fixed by moving the assignment expression into the condition and then 
# referencing the variable name it defined in the comprehension’s 
# value expression:
result = {name: tenth for name, count in stock.items()
          if (tenth := count // 10) > 0}
print(result)

# When uses the walrus operator in the value part of the comprehension and 
# doesn’t have a condition, it’ll leak the loop variable into the 
# containing scope
half = [(last := count // 2) for count in stock.values()]
print(f'Last item of {half} is {last}')

# The leakage is similar to what happens with a normal for loop:
for count in stock.values(): # Leaks loop variable
    pass
print(f'Last item of {list(stock.values())} is {count}')

def the_test():
    half = [count // 2 for count in stock.values()]
    print(half) # Works
    print(count) # Exception because loop variable didn't leak

the_test()

# It’s better not to leak loop variables, so I recommend using assignment 
# expressions only in the condition part of a comprehension.

# Using an assignment expression also works the same way in generator expressions
found = ((name, batches) for name in order
         if (batches := get_batches(stock.get(name, 0), 8)))
print(next(found))
print(next(found))