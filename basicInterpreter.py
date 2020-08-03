#BASIC Interpreter

import sys
variables = dict()          #will keep track of variables and values X = 3

command = []
order = []

for line in sys.stdin:
    line.strip("\n")
    key = int(line[0:3])
    instruction = line[3:].strip("\n")
    order.append([key, instruction])
    command = instruction.split()
    
order = sort(order, key= itemgetter(0))




