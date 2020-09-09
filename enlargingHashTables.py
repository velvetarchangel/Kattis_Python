#enlarging hash tables
#Date: 2020-09-09
#Author: Himika Dastidar

#not optimal times out with very large inputs

import math

def erastosthese_algorithm(N):
    array = [True]*(N+1)
    array[0] = False
    array[1] = False
    
    i = 2
    while(i*i <= N):
        if array[i] is True:
            for j in range(i*2, N+1 , i):
                array[j] = False
        i += 1
    return array
                                                              

#main algorithm
N = int(input())

while (N != 0):
    primes_3n = erastosthese_algorithm(3*N)
    answer = None
    for i in range(2*N, 3*N):
        if (primes_3n[i]):
            answer = i
            break

    if (primes_3n[N]):
        print(answer)
    else:
        print(str(i) + " (" +  str(N) + " is not prime)")
    N = int(input())
