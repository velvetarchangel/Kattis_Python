import random
R, N = [int(x) for x in input().split()]
rooms = [0] * R

for i in range(1, R+1):
  rooms[i-1] = i

for i in range(N):
    booked_room = int(input())
    rooms.remove(booked_room)
    
if len(rooms) == 0:
  print("too late")
else:
  print(rooms[0])
