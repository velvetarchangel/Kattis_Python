import math

num_matches, width, height = [int(x) for x in input().split()]

i = 0

hypotenuse = math.sqrt(width**2 + height**2)

for i in range(num_matches):
    match_size = int(input())
    if match_size <= hypotenuse:
        print("DA")
    else:
        print("NE")
    i += 1
    
