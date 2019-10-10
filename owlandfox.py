num_inputs = int(input())
answer = ""
for i in range(num_inputs):
    number = input()
    input_arr = []
    iter_length = len(number)
    for i in range(iter_length):
        input_arr.append(int(number[i]))
    for i in range(iter_length-1,-1,-1):
        if input_arr[i] != 0:
            input_arr[i] -= 1
            break
    for i in range(len(input_arr)):
        answer += str(input_arr[i])
    if input_arr.count(0) == len(input_arr):
        print("0")
    else:
        print(answer)
    answer = ""
    input_arr = []
