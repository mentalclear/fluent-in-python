a = [1, 2, 3]
b = a 
a.append(4)
print(b)

# Variables boud to objects

class Gizmo:
    def __init__(self) -> None:
        print(f"Gizmo id: {id(self)}")

x = Gizmo()
print(x)

# Returns unsupported operation
# y = Gizmo() * 10
