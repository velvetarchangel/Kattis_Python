K = int(input()) #branch the kitten got stuck
master_list = []
path = []
j = [int(x) for x in input().split()]
while j[0] != -1:
    master_list.append(j)
    j = [int(x) for x in input().split()]

start = K


for i in range (len(master_list)):
    for j in range (len(master_list)):
        if start in master_list[j][1:]:
            path.append(start)
            start = master_list[j][0]
            break
path.append(start)

for i in range(len(path)):
    print(str(path[i]), end = " ")
