#basic programming 1
#Date: 2020-05-23
#Author: Himika Dastidar

def case_1(A):
    return 7

def case_2(A):
    if (A[0] > A[1]): return "Bigger"
    elif (A[0] == A[1]): return "Equal"
    else: return "Smaller"

def case_3(A):
    A_slice = A[0:3]
    A_slice.sort()
    return A_slice[1]

def case_4(A):
    if len(A) == 1: return A[0]
    elif len(A) == 2: return A[0] + A[1]
    else:
        return (case_4(A[0:int(len(A)/2)]) + case_4(A[int(len(A)/2):]))

def case_5(A):
    sumOfEven = 0
    for i in range(len(A)):
        if(A[i] % 2 == 0):
            sumOfEven += A[i]
    return sumOfEven

def case_6(A):
    """
    answer = ""
    for i in range(len(A)):
        answer+= chr((A[i] % 26) + 97)
    return answer
    """
    return ''.join(chr(97+i % 26) for i in A)

def case_7(A):
    i = 0
    visited = [False]*len(A)
    while(True):
        if i >= len(A):
            return "Out"
        if i == len(A)-1:
            return "Done"
        if visited[i] == True:
            return "Cyclic"
        visited[i] = True
        i = A[i]


N, t = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

if t == 1:
    print(case_1(A))
elif t == 2:
    print(case_2(A))
elif t == 3:
    print(case_3(A))
elif t == 4:
    print(case_4(A))
elif t == 5:
    print(case_5(A))
elif t == 6:
    print(case_6(A))
else:
    print(case_7(A))

