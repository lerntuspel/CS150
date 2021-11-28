import string

#Formats the file such that it is a list of lines and each line is a list of words
def organize(file):
  listLines = []
  for aline in file:
    listLines.append(aline.split())
  listLines = removeEmpty(listLines)
  return listLines

#lowercase and un-punctuate all words
def edit(word):
  word = word.lower()
  #remove punctuation
  word = word.strip(string.punctuation)
  word = word.replace(',', '')
  return word

#remove empty lines is a separate function becuase if i try to remove them as we go down the lines editing them, it messes up the current order
def removeEmpty(file):
  for i in range(len(file)):
    try:
      file.remove([])
    except ValueError:
      pass
  return file

def addWord(word, nConcordance):
  #Skip the empty words that used to be punctuation
  if (word==""):
    pass
  #Checks if the word already exists in the dictonary
  elif word in nConcordance.keys():
    nConcordance[word].append(i+1)
  else:
    nConcordance[word] = []
    nConcordance[word].append(i+1)
  return nConcordance

#sort by copy to list and sort alphabetically
def sort(nConcordance):
  ConcordanceAsList = []
  for word in nConcordance:
    ConcordanceAsList.append(word)
  ConcordanceAsList.sort()
  return ConcordanceAsList

Concordance = {}
valid = False
print("Please type in the file you wish to run in the concordance program: ")
while valid==False:
  try:
    inputFile = open(str(input()),"r")
    valid = True
  except FileNotFoundError:
    print("File not found, try again")


oFile = organize(inputFile)
inputFile.close()
#Now it is organized and processed into only lowercase and letters

#loops through all
for i in range(len(oFile)):                     #lines
  for j in range(len(oFile[i])):                  #words
    oFile[i][j] = edit(oFile[i][j])                 #edits words
    Concordance = addWord(oFile[i][j], Concordance) #modifies the concordance

sortedConcordanceKeys = sort(Concordance)

inlines = ""
#loops for each word now in alphabetical order
for a in range(len(sortedConcordanceKeys)):
  inlines = str(Concordance[sortedConcordanceKeys[a]])
  inlines = inlines.strip("[]")
  inlines = inlines.replace(',', '')
  print(sortedConcordanceKeys[a], inlines)

print("I found", len(oFile),"lines containing", len(sortedConcordanceKeys), "unique words.")
input()
