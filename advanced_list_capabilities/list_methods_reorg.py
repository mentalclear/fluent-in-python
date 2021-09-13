# list.sort([key=None] [, reverse=False])
# list.reverse()      # Reverse existing order.

import typing_extensions


def main():
    my_list = []      # Start with empty list
    while True:
        s = input('Enter next name: ')
        if len(s) == 0:
            break
        my_list.append(s)
    my_list.sort()    # Place all elems in order.
    print('Here is the sorted list:')
    for a_word in my_list:
        print(a_word, end=' ')

main()

def ignore_case(s):
    return s.casefold()

a_list = [ 'john', 'paul', 'George', 'brian', 'Ringo' ]
b_list = a_list[:]
a_list.sort()
b_list.sort(key=ignore_case)

print(f"\n{a_list}")
print(f"\n{b_list}")

my_list = ['Brian', 'John', 'Paul', 'George', 'Ringo']
my_list.reverse()    # Reverse elems in place.
for a_word in my_list:
    print(a_word, end=' ')

