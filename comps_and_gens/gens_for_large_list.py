value = [len(x) for x in open('comps_and_gens/my_file.txt')]

print(value)

it = (len(x) for x in open('comps_and_gens/my_file.txt'))
print(it)

print(next(it))

# Used as an input to another generator:
roots = ((x, x** 0.5) for x in it)
print(next(roots))