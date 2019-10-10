N, K= [int(x) for x in input().split()]


def batmanacci(N):
    array_1 = [""]*N
    array_1[0] = "N"
    array_1[1] = "A"

    i = 2
    while(i< N):
        array_1[i] = array_1[i-1] + array_1[i-2]
        i += 1

    return array_1[N-1]

string = batmanacci(N)

print(string[K-1])
