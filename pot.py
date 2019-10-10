N = int(input())

result = 0
str_num = ""
exp = ""

for i in range(N):
    str_input = input()
    for i in range(len(str_input)-1):
        str_num += str_input[i]
    int_num = int(str_num)
    exp = int(str_input[-1])
    result += int_num**exp
    exp = ""
    str_num = ""
print(result)
