word = input()
result = ""
guesses = input()

count = 0
i = 0

while True:
    if len(set(word)) == len(result):
        break
    if count == 10:
        break
    if guesses[i] not in word:
        count += 1
        i += 1
    else:
        result += guesses[i]
        i+=1
        
if count < 10:
    print("WIN")
elif count >= 10:
    print("LOSE")
