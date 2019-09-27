import math
N = int(input())
printers = 1
days = 0

if N == 1:
  print(1)

else:
  while printers < math.ceil(N/2):
    printers *= 2
    days += 1
  print(days + 2)