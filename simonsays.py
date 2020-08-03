#simon says

N = int(input())

for i in range(N):
    sentence = input()
    simonsays = 'simon says '
    if(sentence[:11] == simonsays):
        print(sentence[11:])
    else:
        print("")
