#bounding robots

w, l = [int(x) for x in input().split()]

while w != 0 and l != 0:
    n = int(input())
    actual_x = 0
    actual_y = 0
    robotThinks_x = 0
    robotThinks_y = 0
    for i in range(n):
        direction = input().split()
        move = int(direction[1])
        if(direction[0] == 'u'):
            if (actual_y + move > l-1):
                actual_y = l-1
            else:
                actual_y += move
            robotThinks_y += move
        elif(direction[0] == 'd'):
            if (actual_y - move < 0):
                actual_y = 0
            else:
                actual_y -= move
            robotThinks_y -= move
        elif(direction[0] == 'l'):
            if(actual_x - move < 0):
                actual_x = 0
            else:
                actual_x -= move
            robotThinks_x -= move
        elif(direction[0] == 'r'):
            if(actual_x + move > w-1):
                actual_x = w-1
            else:   
                actual_x += move
            robotThinks_x += move
    print("Robot thinks " + str(robotThinks_x) + " " + str(robotThinks_y))
    print("Actually at " + str(actual_x) + " " + str(actual_y) + "\n")
    w, l = [int(x) for x in input().split()]
    
