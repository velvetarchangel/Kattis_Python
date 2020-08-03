candidates = dict()
name = input()

while name != "***":
    try:
        temp = candidates[name]
        candidates[name] = temp + 1
    except KeyError:
        candidates[name] = 1
    name = input()


sort_candidates = sorted(candidates.items(), key = lambda x: x[1], reverse = True)

if (sort_candidates[0][1] == sort_candidates[1][1]):
    print("Runoff!")
else:
    print(sort_candidates[0][0])
