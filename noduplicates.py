# No duplicates

words = input().split()

set_words = set(words)

if (len(words) - len(set_words) == 0):
    print("yes")
else:
    print("no")

