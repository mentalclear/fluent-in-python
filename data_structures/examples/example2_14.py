# Copies the same list, and the changes now applied to all
# because the are references used.
weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = 'O'
print(weird_board)

# the problem with above code, it behaves like:
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)