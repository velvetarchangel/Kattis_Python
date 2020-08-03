#Jolly Jumpers
import sys
for line in sys.stdin:
    inp = [int(x) for x in line.split()]
    N = inp.pop(0)
    one_through_n_array = [False]*N
    one_through_n_array[0] = True

    for i in range(1, len(inp)):
        difference = abs(inp[i]-inp[i-1])
        if difference >= 1 and difference <= N-1:
            one_through_n_array[difference] = True
        else:
            print("Not jolly")
            break
    set_True = {True}
    if len(set(one_through_n_array).difference(set_True)) == 0:
        print("Jolly")
