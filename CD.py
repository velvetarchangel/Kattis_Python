from sys import stdin

N, M = [int(x) for x in input().split()]

while N != 0 and M !=0:
    jack = set()
    for i in range(N):
        jack.add(int(stdin.readline()))
    coOwned = 0
    for i in range(M):
        temp = int(stdin.readline())
        if temp in jack:
            coOwned += 1
    print(coOwned)
    N, M = [int(x) for x in input().split()]
