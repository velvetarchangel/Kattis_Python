total_players = int(input())

whiteOffence, blackOffence, whiteDefence, blackDefence *queue = input().split()
score = input()

team_white = [whiteOffence, whiteDefence]
team_black = [blackOffence, blackDefence]
white_score = 0
black_score = 0

for i in range(len(score)):
    if score[i] == "W":
        white_score += 1
        if score[i] == score [i-1]:
            temp = whiteDefence
            whiteDefence = whiteOffence
            whiteOffence = temp
        if 
    if score[i] == "B":
        black_score +=1
    
    

