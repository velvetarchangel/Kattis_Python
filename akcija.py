def merge(left, right):
    C = []
    leftIndex = 0
    rightIndex = 0

    while(leftIndex < len(left) and rightIndex < len(right)):
        if(left[leftIndex] > right[rightIndex]):
            C.append(left[leftIndex])
            leftIndex += 1
        else:
            C.append(right[rightIndex])
            rightIndex += 1

    while(leftIndex < len(left)):
        C.append(left[leftIndex])
        leftIndex += 1
    
    while(rightIndex < len(right)):
        C.append(right[rightIndex])
        rightIndex +=1
        
    return C

def mergeSort(arr):
    if(len(arr) == 1): return arr
    left = mergeSort(arr[:int(len(arr)/2)])
    right= mergeSort(arr[int(len(arr)/2):])
    return merge(left, right)


"""driver code"""


N = int(input())

arr = [0]*N

for i in range(N):
    arr[i] = int(input())

arr = mergeSort(arr)
NUMGROUPS = N//3

totalAmount = 0
i = 0

while(i < len(arr)):
    if((i + 1) % 3 != 0):
        totalAmount += arr[i]
    i+= 1
print(totalAmount)
