names = input().split("-")
initials = []

for i in range(len(names)):
    name = names[i]
    initials.append(name[0])
    
for i in range(len(initials)):
    print(str(initials[i]), end = "")
