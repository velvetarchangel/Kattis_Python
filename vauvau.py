#Vauvau

A,B,C,D = [int(x) for x in input().split()]

service = [int(x) for x in input().split()]

dog_1 = [""] * ((A+B)*(max(service)))
dog_2 = [""] * ((C+D)*(max(service)))

d1 = 0
while(d1 < len(dog_1)):
  for j in range(A):
    dog_1[d1] = 1
    d1 += 1
  for k in range(B):
    dog_1[d1] = 0
    d1 += 1

d2 = 0
while(d2 < len(dog_2)):
  for j in range(C):
    dog_2[d2] = 1
    d2 += 1
  for k in range(D):
    dog_2[d2] = 0
    d2 += 1

for i in range(len(service)):
  time_s = service[i] - 1
  if dog_1[time_s] == 1 and dog_2[time_s] == 1:
    print("both")
  elif dog_1[time_s] == 1 or dog_2[time_s] == 1:
    print("one")
  else:
    print("none")
