import sys
import random

arguments = sys.argv

if len(sys.argv) == 1:
    print('insufficient number of arguments. please enter a number of words')
    exit()
    pass
else:
    wordCount = int(sys.argv[1])
    print('creating a sentence with', wordCount, 'number of words')
    # wl = open('/usr/share/dict/words', 'r')
    # wordlist = wl.read()
    # wl.close()
    wordlist = [line.strip() for line in open('/usr/share/dict/words')]
    sentenceArray = []
    for _ in range(0, wordCount):
        tempRandomPosition = random.randint(0, len(wordlist) - 1)
        randomWord = wordlist[tempRandomPosition]
        sentenceArray.append(randomWord)
    sentence = ' '.join(sentenceArray)
    print(sentence, '.')
