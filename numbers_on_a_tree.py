d, path = input().split()

depth = int(d)

array = []
maxValue = 1
for i in reversed(range(-1, depth)):
    n = 2**(i+1)
    arr_t = [0] * n
    for j in reversed(range(n)):
        arr_t[j] = maxValue
        maxValue += 1
    array.insert(0, arr_t)

Level = 0
index = 0
root = array[Level][index]
if path == "":
    print(root)
else:
    for i in range(len(path)):
        if path[i] == "L":
            root = array[1+Level][index]
            Level +=1
        elif path[i] == "R":
            root = array[1+Level][index+1]
            Level+=1
            index += 1
    print(root)
