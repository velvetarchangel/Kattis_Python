N = int(input())

temp = [int(x) for x in input().split()]
current_max = 1000
min_day = 0

for i in range(len(temp)-2):
    
    days = temp[i: i+3] #temp of the day
    rest_day = days[1]
    hiking_days = [days[0],days[2]]
    if max(hiking_days) < current_max:
        current_max = max(hiking_days)
        min_day = i + 1

print(str(min_day) + " " + str(current_max))
