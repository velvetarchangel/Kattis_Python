
def main():
    candidates = []
    votes = []
    name = input()
    while name != "***":
        if name not in candidates:
            candidates.append(name)
            votes.append(1)
        if name in candidates:
            ind = candidates.index(name)
            votes[ind] += 1
        name = input()

    winner = max(votes)
    count = 0

    for i in range(len(votes)):
        if count == 2:
            break
        if votes[i] == winner:
            count += 1

    if count == 1:
        print(candidates[votes.index(winner)])
    elif count == 2:
        print("Runoff!")

main()


        
