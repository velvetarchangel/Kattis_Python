#enlarging hash tables
#Date: 2020-09-09
#Author: Himika Dastidar

#not optimal times out with very large inputs

def is_Prime(N):
    if (N == 2):
        return True
    elif (N % 2) == 0:
        return False
    else:
        i = 3
        while(i*i <= N):
            if (N % i == 0):
                return False
            i += 2
        return True

#main algorithm
N = int(input())

while (N != 0):
    #since 2N will never be a prime
    numToCheck = 2*N + 1
    while(is_Prime(numToCheck) == False):
        numToCheck += 2

    if (is_Prime(N) == True):
        print(numToCheck)
    else:
        print(str(numToCheck) + " (" +  str(N) + " is not prime)")
    N = int(input())
