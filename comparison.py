import sys


def histogramDictionary(short_text):
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


def histogramList(short_text):
    f = open(short_text, 'r')
    histogramList = []
    for line in f:
        for word in line.split():
            index = find(word, histogramList)
            if index == None:
                histogramList.append((word, 1))
            else:
                count = histogramList[index][1]
                new_pair = (word, count + 1)
                histogramList[index] = new_pair
    return histogramList


def find(item, histogramList):
    for index, word in enumerate(histogramList):
        if word[0] == item:
            return index
    return None


def frequencylist(word, histogramList):
    freq = 0
    for index, pair in enumerate(histogramList):
        if pair[0] == word:
            freq = pair[1]
    print('Frequency of the word \'', word, '\' in histogram list is ', freq)
    return freq


def frequencyDict(word, histogramDict):
    freq = 0
    if word in histogramDict:
        freq = histogramDict[word]
    print('Frequency of the word \'', word, '\' in histogram Dictionary is ', freq)
    return freq


def main(argv):

    if len(argv) < 2:
        print('Invalid number of parameters')
        print('Enter text filename to read and word to check frequency')
        sys.exit()
        pass
    else:
        short_text = argv[1]
        wordToLook = argv[2]
        histogram_one = histogramDictionary(short_text)
        histogram_two = histogramList(short_text)
        print('This is histogram one: ', histogram_one)
        print('This is histogram two: ', histogram_two)
        frequencylist(wordToLook, histogram_two)
        frequencyDict(wordToLook, histogram_one)

        pass

if __name__ == "__main__":
    main(sys.argv)
