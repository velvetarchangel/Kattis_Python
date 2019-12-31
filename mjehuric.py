#Mjehuric

initial = [int(x) for x in input().split()]
sorted_arr = sorted(initial)

def swap(index_a, index_b, arr):
  swapped = arr
  temp = swapped[index_a]
  swapped[index_a] = swapped[index_b]
  swapped[index_b] = temp
  return swapped

while initial != sorted_arr:
  if initial[0] > initial[1]:
    initial = swap(0, 1, initial)
    print(' '.join(map(str,initial)))
  if initial[1] > initial[2]:
    initial = swap(1, 2, initial)
    print(' '.join(map(str,initial)))
  if initial[2] > initial[3]:
    initial = swap(2, 3, initial)
    print(' '.join(map(str,initial)))
  if initial[3] > initial[4]:
    initial = swap(3, 4, initial)
    print(' '.join(map(str,initial)))
