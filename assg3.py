def cleanupLine(line):
    # """this function will remove characters that are not needed from the line-string. Unwanted characters are all
    # characters except a-z, A-Z, 0-9 and ' and should be replaced with a space
    #     long-term -> long term
    #     It's amazing, isn't it? -> Is's amazaing  isn't it
    #     Note, if you are familiar with regex, you can use that, otherwise a loop is fine"""
    stripped_line = ""
    for letter in line:
        if 48 <= ord(letter) <= 57 or 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122 or ord(letter) == 39:
            stripped_line += letter
        else:
            stripped_line += ' '
    return stripped_line


def countWords(line, wordsDict=None):
    """For a stripped line, this function counts the words and updates
      the dictionary variable wordsDict{}.
      Note, we convert upper case words to lower case words"""
    for word in line.split():
        if not wordsDict:
            wordsDict = {}
        if word.lower() in wordsDict.keys():
            wordsDict[word.lower()] += 1
        else:
            wordsDict[word.lower()] = 1
    return wordsDict


def countLetters(line, lettersDict=None):
    """For a stripped line, this function counts the letters and updates
          the dictionary variable lettersDict{}.
          Note, we convert upper case letters to lower case
          Note2, numbers and ' should be ignored"""
    if not lettersDict:
        lettersDict = {}
    for word in line.split():
        for letter in word:
            if 48 <= ord(letter) <= 57 or ord(letter) == 39:
                continue
            if letter.lower() in lettersDict:
                lettersDict[letter.lower()] += 1
            else:
                lettersDict[letter.lower()] = 1
    return lettersDict


def readFiles(filename):
    """ This function processes a given file and will return a tuple containing the 
    two dictionaries created"""
    handle = open(filename, 'r')

    for line in handle:
        stripped_line = cleanupLine(line)
        countWords(stripped_line)
        countLetters(stripped_line)

    wordsDict = countWords(stripped_line, wordsDict)
    letterDict = countLetters(stripped_line, letterDict)
    return wordsDict, letterDict


# This is a test function for you:
def results():
    f1w, f1l = readFiles("text1.txt")
    print(f1l['a'])
    print(f1w['the'])


results()
