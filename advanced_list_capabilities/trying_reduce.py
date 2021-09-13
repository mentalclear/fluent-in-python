import functools

def add_func(a, b):
    return a + b

def mul_func(a, b):
    return a * b

n = 5
a_list = list(range(1, n + 1))

triangle_num = functools.reduce(add_func, a_list)
fact_num     = functools.reduce(mul_func, a_list)

print(f"\n{triangle_num} and {fact_num}")