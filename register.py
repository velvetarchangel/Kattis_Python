#primary register

"""
register_ops = [2, 3, 5, 7, 11, 13, 17, 19]
register_capacity = [1, 2, 4, 6, 10, 12, 16, 18]

status = [int(x) for x in input().split()]
operations = 1
for i in range(len(register_ops)):
  if(status[i] != register_capacity[i]):
    operations *= (register_ops[i] - status[i])

print(operations-1)
"""

register_ops = [2, 3, 5, 7, 11, 13, 17, 19]
register_capacity = [1, 2, 4, 6, 10, 12, 16, 18]

status = [int(x) for x in input().split()]

operation = 1

for i in range(len(status)):
    if(status[i] < register_capacity[i]):
        operation *= register_ops[i]
    else:
        operation *= 1
print(operation-1)
