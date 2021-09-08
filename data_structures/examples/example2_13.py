board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

# the above listcomp code is equivalent to this:
board = []
for i in range(3):
    row = ['_'] * 3  
    board.append(row)

print(board)    