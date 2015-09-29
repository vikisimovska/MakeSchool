import sys


def createHistogram(short_text):
    # 'frequency.txt'
    f = open(short_text, 'r')
    histogramDictionary = {}
    for line in f:
        for word in line.split():
            if word in histogramDictionary:
                value = histogramDictionary[word]
                value += 1
            else:
                value = 1
            histogramDictionary[word] = value
    f.close()
    return histogramDictionary


def unique_words(histogram):
    print('Number of unique words: ', len(histogram))


def frequency(word, histogram):
    freq = 0
    if word in histogram:
        freq = histogram[word]
    print('Frequency of the word \'', word, '\' in histogram is ', freq)


def main(argv):

    if len(argv) < 3:
        print('Invalid number of parameters')
        print('Enter text filename to read and word to check frequency')
        sys.exit()
        pass
    else:
        short_text = argv[1]
        histogram = createHistogram(short_text)
        print('Histogram: ', histogram)
        print()
        unique_words(histogram)
        wordToLook = argv[2]
        frequency(wordToLook, histogram)
    pass

if __name__ == "__main__":
    main(sys.argv)
