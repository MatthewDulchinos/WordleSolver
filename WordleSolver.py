#Wordle Solver by Matthew
#Easy program to solve through Wordle games.

#Replace lists with currently known letters
KNOWN_LETTERS = ["h"]
#Each pos should match with the known position of the letter above, or -1 if it is unknown
KNOWN_POS = [1]

#Letters we know not in the word
INVALID_LETTERS = ["c","A","i","r"]

def main():
    #Below line only needs to be uncommented if you lost the trimmed list
    #generateInitList()

    curList = loadInitList()
    for letter in INVALID_LETTERS:
        curList = checkForInvalidLetter(letter, curList)
    for x in range(len(KNOWN_LETTERS)):
        letter = KNOWN_LETTERS[x]
        pos = KNOWN_POS[x]
        if(pos != -1):
            curList = checkForLetterPos(letter, pos, curList)
        else:
            curList = checkForLetterNoPos(letter, curList)
    print(curList)

def generateInitList():
    """Takes a list of words and turns it into possible Wordle words"""
    originalFile = open("word-list-raw.txt", "r")
    trimedFile = open("word-list-trimed.txt", "w")
    for word in originalFile:
        if(len(word) == 6 and word[0:5].isalpha()):
            trimedFile.write(word)
    trimedFile.close()
    originalFile.close()

def loadInitList():
    loadedFile = open("word-list-trimed.txt", "r")

    #remove the annoying \n
    curList = []
    for word in loadedFile:
        curList.append(word[0:5])
    
    return curList

def checkForInvalidLetter(letter, curList):
    shortenedList = []
    for word in curList:
        if(letter.lower() not in word):
            shortenedList.append(word)
    return shortenedList
                

def checkForLetterPos(letter, pos, curList):
    """Eliminate words that don't have the letter at the specific pos in the word"""
    shortenedList = []
    for word in curList:
        if(word[pos] == letter.lower()):
            shortenedList.append(word)
    return shortenedList

def checkForLetterNoPos(letter, curList):
    """Eliminate words that don't have the letter in the word"""
    shortenedList = []
    for word in curList:
        if(letter.lower() in word):
            shortenedList.append(word)
    return shortenedList

main()
