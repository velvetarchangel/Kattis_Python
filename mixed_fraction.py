numerator, denominator = [int(x) for x in input().split()]

while numerator != 0 and denominator != 0:
    quotient = numerator // denominator
    remainder = numerator % denominator
    print(str(quotient) + " " + str(remainder) + " / " + str(denominator))
    numerator, denominator = [int(x) for x in input().split()]
