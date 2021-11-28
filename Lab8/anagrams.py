#anagrams.py
#Alex Yu

import string
#input file validation
#returns the name of the file for future use and the file itself
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

#recycled file formatting functions
def organize(file):
    listLines = []
    for aline in file:
        listLines.append(aline.split())
    listLines = removeEmpty(listLines)
    return listLines

def removeEmpty(file):
    for i in range(len(file)):
        try:
            file.remove([])
        except ValueError:
            pass
    return file

#purpose of the lab
def contains(s, word):
    if (len(word) == 0):
        return True, s
    elif (s.find(word[0])==-1):
        return False, ""
    else:
        return contains((s[:s.index(word[0])]+s[(s.index(word[0])+1):]), word[1:])

def grams(s, words, sofar, max):
#base case
    if ((s=='')and(len(sofar)<=max)):
        output = str(sofar)
        #recycle the trusty .edit created way back when
        print(edit(output))
    for w in words:
        #Still don't really get why making a copy and using .append on the copy breaks it
        copy = sofar + [w]
        isIn, remainder = contains(s, w)
        if isIn==True:
            grams(remainder, words, copy, max)

#extra credit function
def filtr(s, words, min):
    filtered = set()
    for w in words:
        isIn, remainder = contains(s,w)
        if isIn:
            if (len(w)>= min):
                filtered.add(w)
    return filtered

#recycled int validation
def intInput(message, min):
    isint = False
    x = None
    while (isint==False):
        try:
            x = input(message)
            x = int(x)
            if (x>=min):
                isint = True
                return x
            else:
                print("Please enter a number greater or equal to ", (min))
        except ValueError:
            print("Not an integer, Try again.")

def edit(word):
    word = word.lower()
    #remove punctuation
    word = word.strip(string.punctuation)
    word = word.replace(',', '')
    word = word.replace('\'', '')
    return word


fName, file = inputFile("Please enter the filename of a list of words: ")
oFile = organize(file)
file.close()

#loop through the file for words and adds new ones to the set
wordSet = set()
for i in range(len(oFile)):
    for j in range(len(oFile[i])):
        if (oFile[i][j] in wordSet):
            pass
        else:
            wordSet.add(oFile[i][j])

#Strings don't need input validation
print("Enter a word you would Like to see the anagrams of: ")
userInput = edit(input())
userInput = userInput.replace(' ','')

#creates a minimum
print("Enter a minimum size of a word within the anagram")
minimum = intInput('',1)
#creates a maximum
print("Enter a maximum number of word within an anagram")
maximum = intInput('',1)

#reduces the size of the wordList based on the 3 filters that were just input by the user
newWords = filtr(userInput, wordSet, minimum)
#print(newWords)

#makes some anagrams
grams(userInput, newWords, [], maximum)
print()
print("Done!")
input()
