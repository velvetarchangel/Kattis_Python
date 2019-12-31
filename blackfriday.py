#Black Friday

die_roll = [1, 2, 3, 4, 5, 6]
count = [0]*6
unique_entries = []
N = int(input())
entries = [int(x) for x in input().split()]

for i in range(len(entries)):
  count[entries[i]-1] += 1

for i in range(len(count)):
  if count[i] == 1:
    unique_entries.append(i+1)

if len(unique_entries) == 0:
  print("none")
else:
  max_entry = max(unique_entries)
  print(entries.index(max_entry) + 1)
