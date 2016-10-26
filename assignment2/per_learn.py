import os
import json
import random
import sys
from collections import defaultdict,Counter
import time

path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files/train"
# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/Sample/train"
# path = sys.argv[1]
# path=r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment2/Sample/train"
# path=r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment2/files/train"

start_time = time.time()
all_files=defaultdict(int)
all_file_xd=defaultdict(int)
all_files_y=defaultdict()
wd=defaultdict(int)
file_count=0
b=0
maxitr = 20

def readFile(fpath):
    global file_count
    file_count += 1
    xd=defaultdict(int)
    myfile = open(fpath, 'r', encoding="latin1")
    filedata = myfile.read().split()
    if "spam" in fpath:
        key = file_count
        all_files_y[key] = 1
    else:
        key = -file_count
        all_files_y[key] = -1
    all_files[key] = filedata
    for word in filedata:
        if word in wd:
            xd[word]+=1
        else:
            wd[word] = 0
            xd[word] = 1
    all_file_xd[key] = xd


file_read_start = time.time()
for dirName, subdirList, fileList in os.walk(path):
    for fname in fileList:
        fpath = os.path.join(dirName, fname)
        if "DS_Store" in fpath or "__MACOSX" in fpath:
            break
        else:
            readFile(fpath)

mylist = list(all_files.keys())
for i in range(0, maxitr):
    random.shuffle(mylist)
    for fpath in mylist:
        a = 0
        xd = all_file_xd[fpath]
        filedata = all_files[fpath]
        y = all_files_y[fpath]
        a = sum(wd[word] * xd[word] for word in filedata) + b
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

print("---per_learn %s seconds ---" % (time.time() - start_time))





