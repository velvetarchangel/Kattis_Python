import sys

def bringdownOne(k):
    return int(str(k) + str(1))

while True:
    line = sys.stdin.readline()
    if line == '':
        break
    elif line == '\n':
        pass
    else:
        N = int(line)
        k = 1
        count = 1
        remainder = 1
        while(remainder != 0):
            if(remainder < N):
                remainder = bringdownOne(remainder)
                count += 1
            else:
                remainder = remainder % N
        print(count)
