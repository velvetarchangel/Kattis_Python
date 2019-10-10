SETS = int(input())

for i in range(SETS):
    this_set = int(input())
    unique_places = []
    for i in range(this_set):
        place = input()
        if place not in unique_places:
            unique_places.append(place)
        else:
            pass
        place = ""
    print(len(unique_places))
    this_set = 0
    unique_place = []
