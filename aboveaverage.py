cases = int(input())

for i in range(cases):
  
  arr = [int(x) for x in input().split()]
  n = arr.pop(0)
  sum_grades= 0.0

  for i in range(len(arr)):
    sum_grades += arr[i]
  average = sum_grades/len(arr)
  count = 0
  for i in range(len(arr)):
    if arr[i] > average:
      count+= 1
  print('{:.3f}%'.format(100*count/len(arr)))
  arr = []
