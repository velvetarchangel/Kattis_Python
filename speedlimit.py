total_entries = int(input())

distance = 0
prev_time = 0

while total_entries != -1:
    for i in range(total_entries):
        speed, hours = [int(x) for x in input().split()]
        actual_time = hours - prev_time
        distance += speed*actual_time
        prev_time = hours
        i+=1
    print(str(distance) + " miles")
    distance = 0
    prev_time = 0
    total_entries = int(input())
