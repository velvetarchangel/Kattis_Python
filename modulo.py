
unique_mods = []
for i in range(10):
    num = int(input())
    mod_42 = num%42
    if mod_42 in unique_mods:
        pass
    else:
        unique_mods.append(mod_42)
    i+=1
    num = 0
    mod_42 = 0

print(len(unique_mods))

    
