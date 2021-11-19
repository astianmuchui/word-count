file = open('./doc.txt')
words = file.read()
spaces = words.find(' ')
if spaces != -1:
    number_spaces = words.count(' ')
    print('The file has got '+str(number_spaces+1) +' words')
else:
    number_spaces = 0

 
