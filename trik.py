order = input()

initial_array = [1,0,0]

for i in range(len(order)):
    if order[i] == 'A':
        temp = initial_array[0]
        initial_array[0] = initial_array[1]
        initial_array[1] = temp
        
    elif order[i] == 'B':
        temp = initial_array[1]
        initial_array[1] = initial_array[2]
        initial_array[2] = temp
        
    elif order[i] == 'C':
        temp = initial_array[0]
        initial_array[0] = initial_array[2]
        initial_array[2] = temp
    i +=1
    
index_ball = initial_array.index(1) + 1
print(index_ball)
