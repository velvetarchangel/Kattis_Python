#Tajna

string = input()
N = len(string)
R = 1
C = len(string)
decrypted = ""
for i in range(1, len(string)):
  while (R < C):
    R += 1
    if N % R == 0:
      C = int(N/R)

for i in range(C):
  for j in range(R):
    decrypted += string[i + (C)*j]

print(decrypted)
