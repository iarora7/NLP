import os;
import json
import sys

# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files/train"
# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files1"
path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/Sample/train"
# path = sys.argv[1]

wd = dict()
file_count=0
b=0

def readFile(fpath):
	myfile = open(fpath, 'r', encoding='latin1')
	filedata = myfile.read().split()
	for word in filedata:
		word = word.lower()
		if word in wd:
			continue
		else:
			wd[word]=0

for dirName, subdirList, fileList in os.walk(path):
    for fname in fileList:
        fpath = os.path.join(dirName, fname)
        if "DS_Store" in fpath or "__MACOSX" in fpath:
            break
        else:
            file_count += 1
            readFile(fpath)

def computeActivation(fpath):
	a=0
	xd = dict()

	myfile = open(fpath, 'r', encoding='latin1')
	filedata = myfile.read().split()
	if "spam" in fpath:
		y=1
	else:
		y=-1
	for word in filedata:
		if word in xd:
			xd[word] = xd[word]+1
		else:
			xd[word] = 1
	print("xd created:", xd)

	for word in filedata:
		a += (wd[word]*xd[word])
	a = a+b
	if (y*a)<=0:
		wd[word] = wd[word] + (y*xd[word])
		b = b+y


for dirName, subdirList, fileList in os.walk(path):
    for fname in fileList:
        fpath = os.path.join(dirName, fname)
        if "DS_Store" in fpath or "__MACOSX" in fpath:
            break
        else:
        	computeActivation(fpath)
        


print("wd:", wd)
print("b:", b)
print("ham:", file_count)
