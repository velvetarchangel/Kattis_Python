num_test = int(input())

for i in range(num_test):
  sounds = input().split()
  sentence = input()
  my_dict = dict()
  while sentence != "what does the fox say?":
      sent_1 = sentence.split()
      sent_1.remove("goes")
      value = sent_1[0]
      key = sent_1[1]
      my_dict[key] = value
      sentence = input()

  for key in my_dict:
      while key in sounds:
        sounds.remove(key)

  for i in range(len(sounds)):
      print(sounds[i], end= " ")
  sounds = ""
  sentence = ""
  my_dict = ()