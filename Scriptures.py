#365 Scriptures & short message/quote of the scripture


inputFile = open('scriptures.txt','r')

scriptures = []

for value in inputFile.readlines():
    one = value.split('\n')
    message = one[0]
    scriptures.append(message)

