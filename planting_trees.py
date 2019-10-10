n = int(input())
days_to_grow = [int(x) for x in input().split()]
new_list = sorted(days_to_grow, key = int, reverse = True)
days = []
i = 0

for i in range(len(new_list)):
    days.append(new_list[i] + i)

num_days = 2 + max(days)
print(num_days)
