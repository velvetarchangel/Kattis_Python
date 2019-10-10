input_days = int(input())
temp = [int(x) for x in input().split()]
count = 0

for i in range(len(temp)):
    if temp[i] < 0:
        count+=1
print(count)
