#Incomplete, trying to simulate the outcome of the 2048 game



row_1 = [int(x) for x in input().split()]
row_2 = [int(x) for x in input().split()]
row_3 = [int(x) for x in input().split()]
row_4 = [int(x) for x in input().split()]
move = int(input())
board = [row_1, row_2, row_3, row_4]
i = 0
j = 0

#left
if move == 0:
    for i in range(4):
        print(row_1[0],row_1[1],row_1[2],row_1[3])
        print(row_2[0],row_2[1],row_2[2],row_2[3])
        print(row_3[0],row_3[1],row_3[2],row_3[3])
        print(row_4[0],row_4[1],row_4[2],row_4[3])
        if board[i][j] == board[i][j+1]:
            board[i][j] = 2*board[i][j]
            board[i][j+1] = board[i][j+2]
            board[i][j+2] = board[i][j+3]
            board[i][j+3] = 0
        elif (board[i][j] == board[i][j+2] and board[i][j+1] == 0):
            board[i][j] = 2*board[i][j]
            board[i][j+1] = board[i][j+3]
            board[i][j+2] = 0
            board[i][j+3] = 0
        elif (board[i][j] == board[i][j+3] and board[i][j+1] == 0 and board[i][j+2] ==0):
            board[i][j] = 2*board[i][j]
            board[i][j+1] = 0
            board[i][j+2] = 0
            board[i][j+3] = 0

elif move == 1:
    # up
    for j in range(4):
        print(board)
        if board[i][j] == 0:
            board[i][j] = board[i+1][j]
            board[i+1][j] = board[i+2][j]
            board[i+2][j] = board[i+3][j]
            board[i+3][j] = 0
        elif board[i][j] == board[i+1][j]:
            board[i][j] = 2*board[i][j]
            board[i+1][j] = board[i+2][j]
            board[i+2][j] = board[i+3][j]
        elif (board[i][j] == board [i+2][j] and board [i+i][j] == 0):
            board[i][j] = 2*board[i][j]
            board[i+1][j] = board[i+3][j]
            board[i+2][j] = 0
            board[i+3][j] = 0
        elif(board[i][j] == board[i+3][j] and board[i+1][j] == 0 and board[i+2][j] ==0):
            board[i][j] = 2*board[i][j]
            board[i+1][j] = 0
            board[i+2][j] = 0
            board[i+3][j] = 0
            
            

#print(row_1[0],row_1[1],row_1[2],row_1[3])
#print(row_2[0],row_2[1],row_2[2],row_2[3])
#print(row_3[0],row_3[1],row_3[2],row_3[3])
#print(row_4[0],row_4[1],row_4[2],row_4[3])


