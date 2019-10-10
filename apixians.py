name = input()

output = name[0]
for i in range(1, len(name)):
    if name[i] == name[i-1]:
        pass
    else:
        output+=(name[i])
    i+=1

print(output)
