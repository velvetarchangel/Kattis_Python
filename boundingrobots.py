width, length = [int(x) for x in input().split()]

while (width != 0 and length != 0):
    robot_is_x = 0
    robot_is_y = 0
    robot_thinks_x = 0
    robot_thinks_y = 0
    moves = int(input())
    for i in range (moves):
        direction, distance = input().split()
        distance_i = int(distance)
        if(direction == "u"):
            robot_thinks_y += distance_i
            if ((robot_is_y + distance_i) <= length-1):
                robot_is_y += distance_i
            else:
                robot_is_y = length_1
        if (direction == "d"):
            robot_thinks_y += -1*distance_i
            if ((robot_is_y - distance_i) >= 0):
                robot_is_y -= distance_i
            else:
                robot_is_y = 0
        if(direction == "l"):
            robot_thinks_x += -1*distance_i
            if ((robot_is_x - distance_i) >= 0):
                robot_is_x += -1*distance_i
            else:
                robot_is_x = 0
        if(direction == "r"):
            robot_thinks_x += distance_i
            if (distance_i >= width-1):
                robot_is_x = width-1
            else:
                robot_is_x += distance_i
    print("Robot thinks " + str(robot_thinks_x) + " "  + str(robot_thinks_y))
    print("Actually at " + str(robot_is_x) + " " + str(robot_is_y))
    print("")
    width,length = [int(x) for x in input().split()]
            
            
        
