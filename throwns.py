#throwns

n, k = [int(x) for x in input().split()]
instructions = input().split()

current_position = []
i = 0

while i < (len(instructions)):
    if instructions[i] == 'undo':
        current_position = current_position[:-int(instructions[i+1])]
        i+= 2
    else:
        current_position.append(int(instructions[i]))
        i += 1
print(sum(current_position) % n)
