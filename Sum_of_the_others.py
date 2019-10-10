try:
    while True:
        list_1 = [int(x) for x in input().split()]
        answer = sum(list_1)/2
        print(int(answer))
except EOFError:
    pass
