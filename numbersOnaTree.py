inp = input().split()

if len(inp) == 1:
    print(2**(int(inp[0])+1)-1)
else:
    depth = int(inp[0])
    path = inp[1]
    max_value = (2**(depth+1)-1)
    current_index = 0
    for i in range(len(path)):
        if(path[i] == 'R'):
            current_index = current_index*2 + 2
        else:
            current_index = current_index*2 + 1
    print(max_value-current_index)
