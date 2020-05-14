N = int(input())
array_words = []*N
count_doublevowels = []*N
VOWELS = ['a', 'e','i', 'o', 'u', 'y']
while(N != 0):    
    for i in range(N):
        word = input()
        array_words.append(word)
        j = 0
        count_double = 0
        while(j < len(word)-1):
            letter = word[j]
            next_letter = word[j+1]

            if ((letter == next_letter) and (letter in VOWELS)):
                count_double += 1
                j+=2
            else:
                j+=1
        count_doublevowels.append(count_double)
    max_index = 0  
    for i in range(len(count_doublevowels)):
        if(count_doublevowels[i] > count_doublevowels[max_index]):
            max_index = i
    print(array_words[max_index])

    N = int(input())
    array_words = []
    count_doublevowels = []
