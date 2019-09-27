
value = [int(x) for x in input().split()]
output_order = input()
value.sort()

for i in range(len(output_order)):
    if output_order[i] == 'A':
        print(value[0], end =" ")
    if output_order[i] == 'B':
        print(value[1] , end= " ")
    if output_order[i] == 'C':
        print(value[2] , end = " ")
