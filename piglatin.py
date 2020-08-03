import sys

VOWELS = ['a','e', 'i', 'o', 'u', 'y']
for line in sys.stdin:
    words = line.split()
    final_words = []
    for word in words:
        if(word[0] in VOWELS):
           word += 'yay'
           final_words.append(word)
        else:
           temp = ''
           i = 0
           while(word[i] not in VOWELS):
                i+= 1
           temp += word[i:]
           temp += word[0:i]
           temp += 'ay'
           final_words.append(temp)
    for i in range(len(final_words)-1):
        print(final_words[i], end = " ")
    print(final_words[-1])
           
