#standings

N = int(input())

for i in range(N):
    sp = input()
    M = int(input())
    possible_standings = [0]*M
    desired_standings = []

    """
    build up the possible standings array and desired standings array
    """
    for j in range(M):
        team_standing = input().split()
        possible_standings[j] = j+1
        desired_standings.append(int(team_standing[1]))

    """
    now sort the desired standings and compare it to possible standings to
    minimize the difference
    """
    desired_standings.sort()
    result = 0 #badness score
    for j in range(len(possible_standings)):
        result += abs(possible_standings[j]-desired_standings[j])
    print(result)
