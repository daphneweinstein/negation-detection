#use a regex to remove stuff
#tokenize--did this
#stem
#token-type analyze
import nltk
from nltk.stem import *
import operator


fileToRead = ["birmingh2-28160_1.txt.xml", "essexcou1-5166.txt.xml", 
"essexcou1-10460.txt.xml", "foundati1-5205.txt.xml", "heritage1-10767.txt.xml", 
"heritage1-11948.txt.xml", "suffolkc1-6115.txt.xml", "wessexar1-5680.txt.xml", "wessexar1-25626_1.txt.xml"]


def getTypeTok(f):
	

	text = f.read()
	
	tokens = nltk.word_tokenize(text)

	stemmer = PorterStemmer()

	shouldrd = False
	tokenNum = 0
	typeNum = 0
	words = {}
	for token in tokens:
		if "TextWithNodes" in token:
			shouldrd = not shouldrd

		if shouldrd:
			token = token.lower()
			if token.isalpha():
				token = stemmer.stem(token)
				if token in words:
					words[token] = words[token] + 1
				else: 
					typeNum = typeNum + 1
					words[token] = 1
				tokenNum = tokenNum + 1

	#print(typeNum)
	#print(tokenNum)
	print(tokenNum/typeNum)

	#sorted_words = sorted(words.items(), key=operator.itemgetter(1))
	#print(sorted_words)
	
f = open("aocarcha1-GS.xml", "r")
print("aocarcha1-GS.xml")
getTypeTok(f)
f.close()

for fi in fileToRead:
	print(fi)
	f = open(fi, "r", encoding="ISO-8859-1")
	getTypeTok(f)
	f.close()

