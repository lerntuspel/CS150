#recstr.py
import string

def backward(word):
  neWord = ""
  if (len(word)<=1):
    return word
  else:
    return (word[(len(word)-1)] + backward(word[1:(len(word)-1)]) + word[0])

def isPalindrome(word):
    if (len(word)<=1):
        return True
    elif (word[0] == word[len(word)-1]):
        return isPalindrome(word[1:(len(word)-1)])
    else:
        return False

def isSubsequence(word, testWord):
    if len(testWord)==0:
        return True
    elif len(testWord)>len(word):
        return False
    elif (testWord[0]==word[0]):
        return isSubsequence(word[1:len(word)],testWord[1:len(testWord)])
    else:
        return isSubsequence(word[1:len(word)],testWord)

def edit(word):
  word = word.lower()
  #remove punctuation
  word = word.strip(string.punctuation)
  word = word.replace(',', '')
  return word


#print(backward("alligator"))

s = input("Enter a word, s: ")
t = input("Enter a test word, t: ")

s = edit(s)
print(s)
t = edit(t)
print(t)

print("The string \"", s, "\" backwards is \"", backward(s), "\".", sep='')

if isPalindrome(s):
    print("The stirng \"", s, "\" is a palindrome.", sep='')
else:
    print("The stirng \"", s, "\" is not a palindrome.", sep='')

if isSubsequence(s,t):
    print("The stirng \"", t, "\" is a subsequence of \"", s, "\".", sep='')
else:
    print("The stirng \"", t, "\" is not a subsequence of \"", s, "\".", sep='')
