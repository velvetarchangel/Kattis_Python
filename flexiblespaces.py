
W, L = [int(x) for x in input().split()]
bounds = [int(x) for x in input().split()]

possible_configs = set()

possible_configs.add(W)

for i in range(len(bounds)):
    possible_configs.add(W-bounds[i])

for i in range(len(bounds)):
    j = i + 1
    possible_configs.add(bounds[i])
    while(j < len(bounds)):
        possible_configs.add(abs(bounds[i] - bounds[j]))
        j+= 1

arr = list(sorted(possible_configs))

for i in range(len(possible_configs)):
    print(arr[i], end = " ")
