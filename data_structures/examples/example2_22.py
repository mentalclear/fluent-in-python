from collections import deque

dq = deque(range(10), maxlen=10)
print(f"\n{dq}")

# Rotating with n > 0 takes items from the right end 
# and prepends them to the left; 
# when n < 0 items are taken from left and appended to the right.
dq.rotate(3) 
print(f"\n{dq}")

dq.rotate(-4)
print(f"\n{dq}")

dq.appendleft(-1)
print(f"\n{dq}")

dq.extend([11, 22, 33])
print(f"\n{dq}")

dq.extendleft([10, 20, 30, 40])
print(f"\n{dq}")
