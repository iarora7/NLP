import os
import json
import random
import sys
import time
from collections import defaultdict, Counter

# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files/train"
# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/Sample/train"
# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files1"
path = sys.argv[1]
# path=r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment2/Sample/train"
# path=r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment2/files/train"

start_time = time.time()
wd=defaultdict(int)
b=0
ud=defaultdict(int)
beta=0
c=1
all_files=defaultdict()

for dirName, subdirList, fileList in os.walk(path):
    for fname in fileList:
        fpath = os.path.join(dirName, fname)
        if "DS_Store" in fpath or "__MACOSX" in fpath:
            break
        else:
            xd = defaultdict(int)
            myfile = open(fpath, 'r', encoding="latin1")
            filedata = myfile.read().split()
            if "spam" in fpath:
                y = 1
            else:
                y = -1
            for word in filedata:
                if word in wd:
                    # xd[word] += 1
                    continue
                else:
                    wd[word] = 0
                    ud[word] = 0
                    # xd[word] = 1
            all_files[fpath] = {}
            all_files[fpath]['y'] = y
            # all_files[fpath]['data'] = filedata
            all_files[fpath]['xd'] = Counter(filedata)

mylist = list(all_files.keys())
for i in range(0, 30):
    random.shuffle(mylist)
    for fpath in mylist:
        a = 0
        xd = all_files[fpath]['xd']
        # filedata = all_files[fpath]['data']
        y = all_files[fpath]['y']
        a = sum(wd[word] * xd[word] for word in xd) + b
        if (y * a) <= 0:
            for word in xd:
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

model = open('per_model.txt', 'w', encoding="latin1")
model.write(json.dumps(data))
model.close()

print("---avg_per_learn %s seconds ---" % (time.time() - start_time))

