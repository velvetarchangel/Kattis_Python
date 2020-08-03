#2048

import math

row_1 = [int(x) for x in input().split()]
row_2 = [int(x) for x in input().split()]
row_3 = [int(x) for x in input().split()]
row_4 = [int(x) for x in input().split()]
move = int(input())
board = [row_1, row_2, row_3, row_4]
#left
print(board)
if move == 0:
    for i in range(len(board)):
        row = board[i]
        row_set = set(row)
        print(row_set)
#up

elif move == 1:
    pass

#right

elif move == 2:
    pass

#down

elif move == 3:
    pass

print(board)
