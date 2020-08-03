from math import *

rhyme = input().split()

count = int(input())
players = [""]*count
team_1 = []
team_2 = []

for i in range(count):
    players[i] = input()

turn = 1
current_position = 0
while len(players) != 0:
    if turn == 1:
        if len(players) > len(rhyme):
            member_1 = players.pop(current_position + len(rhyme)-1)
            current_position += len(rhyme)-1
        else:
            member_1 = players.pop((current_position + len(players)-1)%len(rhyme))
            current_position = len(players)-1 % len(rhyme)
        team_1.append(member_1)
        turn = 2
    elif turn == 2:
        if len(players) > len(rhyme):
            member_2 = players.pop(current_position + len(rhyme)-1)
            current_position += len(rhyme)-1
        else:
            member_2 = players.pop((current_position + len(players)-1)%len(rhyme))
            current_position = len(players)-1 % len(rhyme)
        team_2.append(member_2)
        turn = 1
    print("team 1 is" + str(team_1))
    print("team 2 is" + str(team_2))
"""

print(len(team_1))
for i in range(len(team_1)):
    print(team_1[i])
print(len(team_2))
for i in range(len(team_2)):
    print(team_2[i]) 
"""
