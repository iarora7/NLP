import os
import json
import random

# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files/train"
# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files1"
# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/Sample/train"
# path = sys.argv[1]
path=r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment2/Sample/train"


wd=dict()
file_count=0
file_list=[]
b=0
maxitr = 25

def readFile(fpath):
    myfile = open(fpath, 'r', encoding="latin1")
    filedata = myfile.read().split()
    for word in filedata:
        word = word.lower()
        if word in wd:
            continue
        else:
            wd[word] = 0

for dirName, subdirList, fileList in os.walk(path):
    for fname in fileList:
        fpath = os.path.join(dirName, fname)
        if "DS_Store" in fpath or "__MACOSX" in fpath:
            break
        else:
            file_count += 1
            file_list.append(fpath)
            readFile(fpath)

for i in range(0, maxitr):
    random.shuffle(file_list)
    for fname in file_list:
        fpath = os.path.join(dirName, fname)
        if "DS_Store" in fpath or "__MACOSX" in fpath:
            break
        else:
            a = 0
            xd = dict()
            myfile = open(fpath, 'r', encoding="latin1")
            filedata = myfile.read().split()
            if "spam" in fpath:
                y = 1
            else:
                y = -1
            # print(filedata)
            for word in filedata:
                if word in xd:
                    xd[word] = xd[word] + 1
                else:
                    xd[word] = 1
            for word in filedata:
                if(word in wd and word in xd):
                    a += (wd[word] * xd[word])
            a = a + b
            if (y * a) <= 0:
                for word in filedata:
                    wd[word] = wd[word] + (y * xd[word])
                b = b + y

data = {
    "b": b,
    "wd": wd
}
json_data = json.dumps(data)
model = open('per_model.txt', 'w')
model.write(json_data)
model.close()

print("filecount:", file_count)





