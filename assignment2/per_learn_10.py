import os
import json
import random
import sys
from collections import defaultdict,Counter
import time

# path = r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files/train"
path = sys.argv[1]
# path=r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment2/files/train"

start_time = time.time()
all_files=defaultdict()
wd=defaultdict(int)
b=0
maxitr = 20
file_count=0
spam_count=0
ham_count=0
spam_limit = 749
ham_limit = 953

file_read_start = time.time()
for dirName, subdirList, fileList in os.walk(path):
    for fname in fileList:
        fpath = os.path.join(dirName, fname)
        if "DS_Store" in fpath or "__MACOSX" in fpath:
            break
        else:
            file_count+=1
            xd = defaultdict(int)
            myfile = open(fpath, 'r', encoding="latin1")
            filedata = myfile.read().split()
            if "spam" in fpath and spam_count < spam_limit:
                spam_count+=1
                y = 1
            elif "ham" in fpath and ham_count < ham_limit:
                ham_count+=1
                y = -1
            else:
                break
            for word in filedata:
                if word in wd:
                    continue
                else:
                    wd[word] = 0
            all_files[fpath] = {}
            all_files[fpath]['y'] = y
            all_files[fpath]['xd'] = Counter(filedata)

mylist = list(all_files.keys())
for i in range(0, maxitr):
    random.shuffle(mylist)
    for fpath in mylist:
        a = 0
        xd = all_files[fpath]['xd']
        y = all_files[fpath]['y']
        a = sum(wd[word] * xd[word] for word in xd) + b
        if (y * a) <= 0:
            for word in xd:
                wd[word] = wd[word] + (y * xd[word])
            b = b + y

data = {
    "b": b,
    "wd": wd
}
model = open('per_model.txt', 'w', encoding="latin1")
model.write(json.dumps(data))
model.close()

print(file_count)
print("spams:", spam_count)
print("hams:", ham_count)
print("---per_learn %s seconds ---" % (time.time() - start_time))





