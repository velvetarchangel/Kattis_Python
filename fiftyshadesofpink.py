N = int(input())

count = 0
for i in range(N):
    word = input().lower()
    if(('rose' in word) or ('pink' in word)):
        count += 1
    
if count > 0:
    print(count)
else:
    print("I must watch Star Wars with my daughter")
