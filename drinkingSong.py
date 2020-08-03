#drinkingSong
#Date: 20200523
#Author: Himika

N = int(input())
liquid = input()


i = N

bottlesOf = " bottles of "
onTheWall = " on the wall, "
takeOne = "Take one down, pass it around, "
onTheWallEnd = " on the wall."

while(i > 0):
    if(i > 2):
        print(str(i) + bottlesOf + liquid + " on the wall, " + str(i) + bottlesOf + liquid + ".")
        print(takeOne + str(i-1) + bottlesOf + liquid + onTheWallEnd + "\n")
    elif (i == 2):
        print(str(i) + bottlesOf + liquid + onTheWall + str(i) + bottlesOf + liquid + ".")
        print(takeOne + "1 bottle of " + liquid + onTheWallEnd + "\n")
        
    elif(i == 1):
        print("1 bottle of " + liquid + onTheWall + "1 bottle of " + liquid + ".")
        print("Take it down, pass it around, no more bottles of " + liquid + ".")
    i -= 1
