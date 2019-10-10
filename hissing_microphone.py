word = input()
a = "no hiss"
for i in range(len(word)-1):
    if (word[i] == 's' and word[i+1] == 's'):
        a = "hiss"
        break
    else:
        i+=1
print(a)
