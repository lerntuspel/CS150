#distill.py
#ALex Yu
import string
#using concordance from lab 6 as a foundation
#organize function from concordance that makes a File
#into list of lines and each line into a list of words
def organize(file):
    listLines = []
    for aline in file:
        listLines.append(aline.split())
    for i in range(len(listLines)):
        try:
            listLines.remove([])
        except ValueError:
            pass
    return listLines

def edit(word):
    word = word.lower()
    #remove punctuation
    word = word.strip(string.punctuation)
    word = word.replace(',', '')
    return word

#sort by copy to list and sort alphabetically
def alphaSort(wordDict):
    dictAsList = []
    for word in wordDict:
        dictAsList.append(word)
    dictAsList.sort()
    wordListTwo = {}
    for i in range(len(dictAsList)):
        wordListTwo[dictAsList[i]] = wordDict[dictAsList[i]]
    return wordListTwo

#insersion sort
def numSort(wordDict):
    dictAsStrList = []
    dictAsNumList = []
    for word in wordDict:
        dictAsNumList.append(wordDict[word])
        dictAsStrList.append(word)
    return insertSort(dictAsNumList, dictAsStrList)

#takes in a list of numbers and corresponding words
def insertSort(baList, coList):
    for i in range (1,len(baList)):
        #set current index as smallest to be compared to
        value = baList[i]
        word = coList[i]
        j = i - 1
        while (j>=0):
            #replacement by the larger one
            if (value > baList[j]):
                baList[j+1] = baList[j]
                coList[j+1] = coList[j]
                baList[j] = value
                coList[j] = word
                j = j - 1
            else:
                break
    #coList was sorted into the same order as its corresponding values in the original dicitonary
    return baList, coList

#word counter counts how many times each word appears
def addWordCount(word, wordList):
#Skip the empty words that used to be punctuation
    if (word==""):
        pass
#Checks if the word already exists in the dictonary
    elif word in wordList.keys():
        wordList[word] = wordList[word] + 1
    else:
        wordList[word] = 1
    return wordList

def intInput(message, min, max):
    isint = False
    x = None
    while (isint==False):
        try:
            x = input(message)
            x = int(x)
            if ((x>=min)and(x<=max)):
                isint = True
                return x
            else:
                print("Please enter a number greater than or equal to ", (min), " and less or equal to ", (max))
        except ValueError:
            print("Not an integer, Try again.")

#File validation
def inputFile(message):
    valid = False
    print(message)
    while valid==False:
        try:
            fileName = str(input())
            if (".txt" in fileName):
                inFile = open(fileName,"r")
                valid = True
            else:
                print("Wrong file type, try again")
#            fileName = "words1.txt"
#            inFile = open("words1.txt", "r")
        except FileNotFoundError:
            print("File not found, try again")
    return fileName, inFile

fName, file = inputFile("Please enter the filename of the file you want to distill: ")
oFile = organize(file)
file.close()
#Now it is organized and processed into only lowercase and letters
wordCount = {}
#loops through all
for i in range(len(oFile)):                     #lines
  for j in range(len(oFile[i])):                  #words
    oFile[i][j] = edit(oFile[i][j])                 #edits words
    wordCount = addWordCount(oFile[i][j], wordCount)   #adds to the word's counter
numList, strList = numSort(alphaSort(wordCount))
#test number
commonWords = []
n = intInput("Enter the number of common words you wish to remove: ", 1, len(wordCount))
for i in range(n):
    commonWords.append(strList[i])
#print("Common Words:")
#print(commonWords)
#reprint
#print("Old Poem")
oldFile = open(fName,"r")
disPoem = organize(oldFile)
oldFile.close()
#print(disPoem)
print()
print("New Poem:")
print()
for i in range(len(disPoem)):                     #lines
    for j in range(len(disPoem[i])):                  #words
        word = edit(disPoem[i][j])                 #edits words
        if word in commonWords:
            pass
        elif word=='':
            pass
        else:
            print(disPoem[i][j] + " ", end='')
    print()
input()
