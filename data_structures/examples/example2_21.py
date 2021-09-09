import numpy as np

a = np.arange(12)
print(a)
print(type(a))

print(a.shape)

a.shape= 3, 4
print(f"\n{a}")

print(f"\n{a[2]}")

print(f"\n{a[2, 1]}")

print(f"\n{a[:, 1]}")

print(f"\n{a.transpose()}")