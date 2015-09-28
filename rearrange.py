import random
import sys


arguments = sys.argv
words = arguments[1:]

newRanomizedArray = []

while len(words) > 0:
    tempRandomPosition = random.randint(0, len(words) - 1)
    newRanomizedArray.append(words[tempRandomPosition])
    del words[tempRandomPosition]
    pass

print(newRanomizedArray)

# learning how to commit on development branch
