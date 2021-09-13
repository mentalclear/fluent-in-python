# list.append(value)         # Append a value
# list.clear()               # Remove all contents
# list.extend(iterable)      # Append a series of values
# list.insert(index, value)  # At index, insert value
# list.remove(value)         # Remove first instance of
#                            #  value

abc_list = ["A", "B", "C"]
print(f"\n{abc_list}")

abc_list.clear()
print(f"\n{abc_list}")

abc_list.append("D")
print(f"\n{abc_list}")

abc_list.extend(["E", "F", "G"])
print(f"\n{abc_list}")

a_list = [10, 20, 40]  # Missing 30.
a_list.insert(2, 30 )  # At index 2 (third), insert 30.
print(a_list)          # Prints [10, 20, 30, 40]
a_list.insert(100, 33)
print(a_list)          # Prints [10, 20, 30, 40, 33]
a_list.insert(-100, 44)
print(a_list)          # Prints [44, 10, 20, 30, 40, 33]

my_list = [15, 25, 15, 25]
my_list.remove(25)
print(my_list)         # Prints [15, 15, 25]
