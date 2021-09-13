
import functools

my_f = lambda x, y: x + y

print(f"\n{my_f(1, 2)}")

print(f"\n{my_f(5, 5)}")

t5 = functools.reduce(lambda x, y: x + y, [1,2,3,4,5])
print(f"\n{t5}")

f5 = functools.reduce(lambda x, y: x * y, [1,2,3,4,5])
print(f"\n{f5}")