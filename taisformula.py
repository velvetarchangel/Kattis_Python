#Tai's formula

N = int(input())
array = []
glucose_reading = 0
for i in range(N):
    arr = [0]*2
    t, g = [float(x) for x in input().split()]
    arr[0] = t
    arr[1] = g
    array.append(arr)
    arr = [0]*2

for i in range(N-1):
    glucose_reading += (((array[i][1] + array[i+1][1])/2)*(array[i+1][0]-array[i][0])/1000)
print(glucose_reading)
