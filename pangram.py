#PANGRAM

is_pangram = set(('abcdefghijklmnopqrstuvwxyz'))
N = int(input())

for i in range(N):
    input_text = input()
    set_input = set(input_text.lower())
    answer = list(is_pangram.difference(set_input))
    if len(answer) == 0:
        print('pangram')
    else:
        print("missing ", end = '')
        answer.sort()
        for i in answer:
            print(i, end = '')
        print("")
