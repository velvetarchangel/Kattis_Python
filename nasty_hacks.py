num_cases = int(input())

for i in range(num_cases):
    r, c, e = [int(x) for x in input().split()]
    if r + e > c:
        print("do not advertise")
    elif r + e == c:
        print("does not matter")
    elif r + e < c:
        print("advertise")
