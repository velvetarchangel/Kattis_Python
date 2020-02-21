N = int(input())

for i in range(N):
    sentence = input()
    if len(sentence) > 0:
        test = sentence.split()
        if test[0] == "simon" and test[1] == "says":
          for j in range(2, len(test)):
            print(test[j] , end = " ")
        else:
          print("")
    else:
        pass


