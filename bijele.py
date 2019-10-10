actual = [int(x) for x in input().split()]

expected = [1,1,2,2,2,8]

difference = []

for i in range(len(actual)):
    diff = expected[i] - actual[i]
    difference.append(diff)

for i in range(len(difference)):
    print(difference[i], end = " ")
