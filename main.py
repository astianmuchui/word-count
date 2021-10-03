file = open('./doc.txt')
words = file.read()
print(words)
spaces = words.find(' ')
if spaces != -1:
    number_spaces = words.count(' ')
    print('The file has '+str(number_spaces+1) +' words')
else:
    number_spaces = 0

 