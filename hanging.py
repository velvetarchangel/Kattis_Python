capacity,length = [int(x) for x in input().split()]
number_on_terrace = 0
groups_rejected = 0
for i in range(length):
    stringOne, numberTwo = input().split()
    coming_going = int(numberTwo)
    if (stringOne == "enter" and ((coming_going + number_on_terrace) > capacity)):
        groups_rejected += 1
    elif (stringOne == "enter" and ((coming_going + number_on_terrace) <= capacity)):
        number_on_terrace += coming_going
    else:
        number_on_terrace -= coming_going
print(groups_rejected)
