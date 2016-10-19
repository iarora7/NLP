import os
import json
import random
import sys
import time
from collections import defaultdict

# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files/train"
# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files1"
# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/Sample/train"
path = sys.argv[1]
# path=r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment2/Sample/train"
# path=r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment2/files/train"

start_time = time.time()
wd=defaultdict(int)
b=0
ud=defaultdict(int)
beta=0
c=1
file_count=0
file_list=[]
maxitr = 2
all_files=dict()

def readFile(fpath):
    myfile = open(fpath, 'r', encoding="latin1")
    filedata = myfile.read().split()
    all_files[fpath] = filedata
    for word in filedata:
        word = word.lower()
        if word in wd:
            continue
        else:
            wd[word] = 0
            ud[word] = 0

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
    for fpath in file_list:
        a = 0
        xd = defaultdict(int)
        filedata = all_files[fpath]
        if "spam" in fpath:
            y = 1
        else:
            y = -1
        # calculate xd (vector of input data features)
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
                ud[word] = ud[word] + (y * c * xd[word])
            b = b + y
            beta = beta + (y*c)
        c = c + 1

for k,v in ud.items():
    ud[k] = wd[k] - ((1/c) * ud[k])

beta = b - ((1/c) * beta)

data = {
    "b": beta,
    "wd": ud
}
json_data = json.dumps(data)
model = open('per_model.txt', 'w')
model.write(json_data)
model.close()

print("filecount:", file_count)
print("--- %s seconds ---" % (time.time() - start_time))

