#Judging Moose
#Author: Himika Dastidar
#Date Dec 25, 2019


l, r = [int(x) for x in input().split()]

if l == 0 and r == 0:
    print("Not a moose")

elif l > r:
    print("Odd " + str(2*l))
elif r > l:
    print("Odd " + str(2*r))
else:
    print("Even " + str(2*l))
