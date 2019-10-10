N = int(input())
sum = 0
for i in range(N):
    numberOne, numberTwo = [float(x) for x in input().split()]
    intermed = numberOne*numberTwo
    sum+= intermed
print(sum)
