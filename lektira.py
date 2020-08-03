#Lektira
import math

ORIGINAL_WORD = input()
words_after_altering = []   #array to keep track of words generated after altering

words_before_reversing = []

for i in range(math.ceil(len(ORIGINAL_WORD)/2)):
    for j in range(len(ORIGINAL_WORD), math.floor(len(ORIGINAL_WORD)/2), -1):
        word_1 = ORIGINAL_WORD[0:i]
        words_before_reversing.append(word_1)
        word_2 = ORIGINAL_WORD[i:j]
        words_before_reversing.append(word_2)
        word_3 = ORIGINAL_WORD[j:]
        words_before_reversing.append(word_3)
        #reverse the words
        word = ""
        for w in range(len(words_before_reversing)):
            word += words_before_reversing[w][::-1]
        words_after_altering.append(word)
        words_before_reversing = []
words_after_altering.sort()
print(words_after_altering)
print(words_after_altering[0])
