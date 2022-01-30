from textblob import TextBlob
from spellchecker import SpellChecker
import re
file1="mobydick.txt"
with open(file1,"r+") as filehandle:
    filecontent=filehandle.read()
    print("Original Text:\n", str(filecontent))
    b = TextBlob(filecontent)
    #print("Corrected text:\n", str(b.correct()))

#remove all punctuations before finding possible misspelled words
s = re.sub(r'[^\w\s]','',filecontent)
#print("Text without punctuations:\n",s)
wordlist=s.split()
spell = SpellChecker()
# find those words that may be misspelled
misspelled = list(spell.unknown(wordlist))
print("Possible list of misspelled words in the original text:\n",misspelled)
#textblob cannot correct all misspellings , some corrections might be meaningless, so its important to find all candidate words
for word in misspelled:
    print(word)
    # Get the one `most likely` answer
    print("Correct word:",spell.correction(word))
    # Get a list of `likely` options
    print("Candidate words:",spell.candidates(word))
