N = int(input())
array = [int(x) for x in input().split()]
array.sort()
for i in range(2):
    array.append(0)
result = []
i = 0

print(array)
for i in range(N):
    if (array[i+1] == array[i]+1 and array[i+2] == array[i]+2):
        n = i
        while (array[i + n] == array[i]+n):
            n +=1
        result.append(str(array[i])+"-"+ str(array[i+n-1]))
        
        n = 0
    else:
        result.append(array[i])
        i+=1

for i in range(N):
    print(result[i], end= " ")
