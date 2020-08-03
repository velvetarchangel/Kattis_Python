S = input()
P = input()

def reverseCase(P, S):
    rev = ''
    for i in range(len(S)):
        if(S[i].isupper()):
            rev += S[i].lower()
        elif(S[i].islower()):
            rev += S[i].upper()
        else:
            rev += S[i]
    return (rev == P)

def appendAndPrepend(P, S):
    for i in range(10):
        temp_1 = str(i) + P
        temp_2 = P + str(i)
        if(temp_1 == S or temp_2 == S):
            return True
    return False


if (S == P):
    print("Yes")
elif(reverseCase(P, S) == True or appendAndPrepend(P,S) == True):
    print("Yes")
else:
    print("No")

