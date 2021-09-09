# Example 2-19. Handling 6 bytes memory of as 1×6, 2×3, and 3×2 views

from array import array
octets = array('B', range(6))
m1 = memoryview(octets)
print(m1.tolist())

m2 = m1.cast('B', [2,3])
print(m2.tolist())

m3 = m1.cast('B', [3,2])
print(m3.tolist())

m2[1,1] = 22
m3[1,1] = 33
print(octets)