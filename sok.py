total_drinks = [int(x) for x in input().split()]
ratio_drinks = [int(x) for x in input().split()]

num_drinks = []

for i in range(len(total_drinks)):
    num_drinks.append(total_drinks[i]/ratio_drinks[i])
    
min_drinks = min(num_drinks)
index_high = num_drinks.index(min_drinks)

balance = []

for i in range(len(total_drinks)):
    leftover = total_drinks[i] - min_drinks*ratio_drinks[i]
    balance.append(leftover)

print(str(balance[0])+ " " + str(balance[1]) + " " + str(balance[2]))
