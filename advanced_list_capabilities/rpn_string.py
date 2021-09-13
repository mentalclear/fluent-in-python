the_stack = []

# completed full refactoring

def main():
    s = input('Enter RPN string: ')
    a_list = s.split()
    for item in a_list:
        if item in '+-*/':
            op2 = the_stack.pop()
            op1 = the_stack.pop()
            the_stack.append(eval(str(op1) + item + str(op2)))
        else:
            the_stack.append(float(item))
    print(the_stack.pop())

main()


# Refactored  with eval
# def push(v):
#     the_stack.append(v)

# def pop():
#     return the_stack.pop()

# def main():
#     s = input('Enter RPN string: ')
#     a_list = s.split()
#     for item in a_list:
#         if item in '+-*/':
#             op2 = pop()
#             op1 = pop()
#             push(eval(str(op1) + item + str(op2)))
#         else:
#             push(float(item))
#     print(pop())

# main()


# Refactored 1
# def main():
#     s = input('Enter RPN string: ')
#     a_list = s.split()
#     for item in a_list:
#         if item in '+-*/':
#             op2 = the_stack.pop()
#             op1 = the_stack.pop()
#             if item == '+':
#                 the_stack.append(op1 + op2)
#             elif item == '-':
#                 the_stack.append(op1 - op2)
#             elif item == '*':
#                 the_stack.append(op1 * op2)
#             else:
#                 the_stack.append(op1 / op2)
#         else:
#             the_stack.append(float(item))
#     print(the_stack.pop())


# def push(v):
#     the_stack.append(v)

# def pop():
#     return the_stack.pop()

# def main():
#     s = input('Enter RPN string: ')
#     a_list = s.split()
#     for item in a_list:
#         if item in '+-*/':
#             op2 = pop()
#             op1 = pop()
#             if item == '+':
#                 push(op1 + op2)
#             elif item == '-':
#                 push(op1 - op2)
#             elif item == '*':
#                 push(op1 * op2)
#             else:
#                 push(op1 / op2)
#         else:
#             push(float(item))
#     print(pop())

