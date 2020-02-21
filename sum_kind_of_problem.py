#Sum Kind of Problem

P = int(input())

for i in range(P):
    K, N = [int(x) for x in input().split()]

    #SUM OF N numbers from 1-n = N(N+1)/2
    S1 = int(N*(N+1)/2)
    S2 = N*N
    S3 = int(N*(N+1))
    
    
    print(str(K) + " " + str(S1) + " " + str(S2) + " " + str(S3))
