import os
import json
import random
import sys
import time
from collections import defaultdict, Counter

# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files/train"
path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/Sample/train"
# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files1"
# path = sys.argv[1]
# path=r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment2/Sample/train"
# path=r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment2/files/train"

start_time = time.time()
wd=defaultdict(int)
b=0
ud=defaultdict(int)
beta=0
c=1
file_count=0
maxitr = 30
all_files=defaultdict(int)


def readFile(fpath):
    global file_count
    file_count += 1
    xd = defaultdict(int)
    myfile = open(fpath, 'r', encoding="latin1")
    filedata = myfile.read().split()
    if "spam" in fpath:
        key = file_count
        y = 1
    else:
        key = -file_count
        y = -1
    all_files[key]['y'] = y
    all_files[key]["data"] = filedata
    for word in filedata:
        if word in wd:
            xd[word] += 1
        else:
            wd[word] = 0
            ud[word] = 0
            xd[word] = 1
    all_files[key].setdefault('xd', xd)
    # all_files[key][xd] =
    print(all_files[key])

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
        xd = all_files[fpath]['xd']
        filedata = all_files[fpath]['data']
        y = all_files[fpath]['y']
        a = sum(wd[word] * xd[word] for word in filedata) + b
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

# if(os.path.isfile('per_model.txt')):
#     os.remove('per_model.txt')
#     print("removed")

model = open('per_model.txt', 'w')
model.write(json_data)
model.close()

print("---avg_per_learn %s seconds ---" % (time.time() - start_time))

