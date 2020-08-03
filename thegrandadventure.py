N = int(input())

for i in range(N):
  path = input()
  bag = []
  j = 0
  isYesInstance = 'YES'
  while j < len(path):
    if(path[j] == "$" or path[j] == "*" or path[j] == "|"):
      bag.append(path[j])
    elif((path[j] == 'j' or path[j] == 't' or path[j] == 'b') and len(bag) == 0):
        isYesInstance = 'NO'
    elif((path[j] == 't' and len(bag)!= 0) and bag.pop() != '|'): 
      isYesInstance = 'NO'
    elif((path[j]=='j' and len(bag)!= 0) and bag.pop() != '*'): 
      isYesInstance = 'NO'
    elif((path[j] == 'b' and len(bag)!= 0) and bag.pop() != '$'): 
      isYesInstance = 'NO'
    j+= 1
  if(len(bag) != 0):
    isYesInstance = 'NO'
  print(isYesInstance)
