#Erase Securely

N = int(input())

original_file = input()
changed_file = input()
expected_file = ""

if (N % 2 == 0):
  expected_file = original_file
else:
  for i in range(len(original_file)):
    if original_file[i] == "1":
      expected_file += "0"
    else:
      expected_file += "1"

#print(expected_file)
deleted = "Deletion succeeded"

for i in range(len(expected_file)):
  if expected_file[i] != changed_file[i]:
    deleted = "Deletion failed"
print(deleted)
