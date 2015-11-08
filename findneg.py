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

stemmer = PorterStemmer()
tokenNum = 0
typeNum = 0
words = {}
shouldrd = False

neg = 0
#process aocarcha1
f = open("aocarcha1-GS.xml", "r")
print()
print()
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("aocarcha1-GS.xml")
shouldrd = False
for line in f.readlines():
	if "TextWithNodes" in line:
		shouldrd = not shouldrd
	if shouldrd:
		if "<Node" in line:
			#print(line)
			neg = neg + 1

f.close()

#process the remaining files
for fi in fileToRead:
	print()
	print()
	print()
	print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
	print(fi)
	f = open(fi, "r", encoding="ISO-8859-1")
	shouldrd = False
	for line in f.readlines():
		if "TextWithNodes" in line:
			shouldrd = not shouldrd
		if shouldrd:
			if "<Node" in line:
				#print(line)
				neg = neg + 1

	f.close()

print(neg)




