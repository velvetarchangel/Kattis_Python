string_array = ["helloworld", "monkey", "bunny"]
word = ''
for i in range(len(string_array)):
    word += string_array[i][::-1]
print(word)
