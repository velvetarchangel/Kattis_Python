import math
height, angle = [int(x)for x in input().split()]

length_ladder = height/math.sin(math.radians(angle))

if length_ladder%1 > 0:
    print(int(length_ladder//1 + 1))
else:
    print(int(length_ladder))
