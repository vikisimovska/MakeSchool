import random

import sys


def createHistogram(fish):
    # 'frequency.txt'
    f = open(fish, 'r')
    # file_string = f.read()
    # print(file_string)
    histogramDictionary = {}
    for line in f:
        for word in line.split():
            value = 1
            if word in histogramDictionary:
                value = histogramDictionary[word]
                value += 1
            histogramDictionary[word] = value
    f.close()
    return histogramDictionary


def spitOneWord(histogram):
    randWordPosition = random.randint(0, len(histogram) - 1)
    randWord = list(histogram.keys())
    word = randWord[randWordPosition]
    print(word)


def main(argv):

    if len(argv) < 2:
        sys.exit()
        pass

    else:

        fish = argv[1]
        print('file name ' + fish)
        histogram = createHistogram(fish)
        print('Histogram: ', histogram)
        print()
        spitOneWord(histogram)

        pass


if __name__ == "__main__":
    main(sys.argv)
