import os;
import json
import sys

path = r"/Users/isha/USC/sem3/NLP/assignments/nlp/assignment1/files/train"
# path = r"/Users/isha/USC/sem3/NLP/assignments/nlp/assignment1/Sample/train"
# path = sys.argv[1]

vocab = set()
ham_dict = {}
spam_dict = {}
spam_file_count = 0
ham_file_count = 0

def readFile(fpath, label_dict):
    myfile = open(fpath, 'r', encoding='latin1')
    filedata = myfile.read().split()
    for word in filedata:
        # word = word.lower()
        vocab.add(word)
        if word in label_dict:
            label_dict[word] += 1
        else:
            label_dict[word] = 1


for dirName, subdirList, fileList in os.walk(path):
    for fname in fileList:
        fpath = os.path.join(dirName, fname)
        if "DS_Store" in fpath:
            break
        if "ham" in fpath:
            label_dict = ham_dict
            ham_file_count += 1
        else:
            label_dict = spam_dict
            spam_file_count += 1
        readFile(fpath, label_dict)


spam_wc = 0
ham_wc = 0

for key in ham_dict:
    ham_wc += ham_dict[key]
for key in spam_dict:
    spam_wc += spam_dict[key]

data = {
    "ham_file_count": ham_file_count,
    "spam_file_count": spam_file_count,
    "spam_wc":spam_wc,
    "ham_wc":ham_wc,
    "vocab_wc":len(vocab),
    "spam_dict": spam_dict,
    "ham_dict": ham_dict
}

json_data = json.dumps(data)

model = open('nbmodel.txt', 'w')
model.write(json_data)
model.close()
