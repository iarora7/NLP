import json;
import sys
import os
import time

# path = sys.argv[1]
# opfile = sys.argv[2]
opfile = 'per_output.txt'
path=r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/files/dev"
# path=r"/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/Sample/test"
# path=r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment2/files/dev"

start_time = time.time()
wd=dict()
b = 0
op = 0
all_files=dict()
file_count=0

output_file = open(opfile, 'w')

model_file = open("per_model.txt", 'r', encoding="latin1")
file_data = model_file.read()
model_file.close()
file_data = json.loads(file_data)
for k in file_data:
    if (k == "b"):
        b = file_data[k]
    if (k == "wd"):
        wd = file_data[k]

for dirName, subdirList, fileList in os.walk(path):
    for fname in fileList:
        fpath = os.path.join(dirName, fname)
        if "DS_Store" in fpath or "__MACOSX" in fpath:
            break
        else:
            a = 0
            xd = dict()
            myfile = open(fpath, 'r', encoding="latin1")
            file_count += 1
            filedata = myfile.read().split()
            for word in filedata:
                if word in xd:
                    xd[word] = xd[word] + 1
                else:
                    xd[word] = 1
            for word in xd:
                if (word in wd and word in xd):
                    a += (wd[word] * xd[word])
            a = a + b
            if (a > 0):
                op = "SPAM"
            else:
                op = "HAM"
            output_file.write(op + " " + fpath + "\n")


output_file.close()

print(file_count)
print("---per_classify %s seconds ---" % (time.time() - start_time))
