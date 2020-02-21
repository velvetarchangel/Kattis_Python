from itertools import combinations

arr = [0]*9
final_arr = [0]*7

s = 0 #sum
for i in range(9):
    arr[i] = int(input())

comb = combinations(arr, 7)
for i in list(comb):
    for j in range(len(i)):
        s += i[j]
    if s == 100:
        for k in range(7):
            print(i[k])
    else:
            s = 0

