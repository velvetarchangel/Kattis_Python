import heapq

cities, boxes = [int(x) for x in input().split()]
population = []
boxes_assigned = []
votes_per_box = []

while cities != -1 and boxes != -1:
    for i in range(cities):
        population.append(input)
        boxes_assigned.append(1)
    votes_per_box[i] = population[i])
    boxes -= 1

    print(votes_per_box)

    while boxes != 0:
        max_votes = max(votes_per_box)
        index_max = votes_per_box.index(max_votes)
        boxes_assigned[index_max] += 1
        boxes -= 1
        for i in range(cities):
            votes_per_box[i] = population[i]/boxes_assigned[i]

    if input == " ":
        print(max_votes)
