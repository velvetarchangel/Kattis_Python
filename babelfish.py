english = []
foreign = []

inp = input()
while inp != "":
    e, f = inp.split()
    english.append(e)
    foreign.append(f)
    inp = input()

word = input()
while word != "":
    if word in foreign:
        w_index = foreign.index(word)
        print(english[w_index])
    else:
        print("eh")
    word = input()
