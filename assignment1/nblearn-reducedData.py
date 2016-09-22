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

spam_file_limit = 749
ham_file_limit = 953

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
        # if "DS_Store" in fpath:
        #     break

        # exit for loop after
        if(ham_file_count>ham_file_limit and spam_file_count>spam_file_limit):
            break

        if "ham" in fpath:
            if(ham_file_count < ham_file_limit):
                ham_file_count += 1
                label_dict = ham_dict
            else:
                break
        else:
            if(spam_file_count < spam_file_limit):
                label_dict = spam_dict
                spam_file_count += 1
            else:
                break
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

print("vocab_wc:", len(vocab))
print("spam_file_count:",spam_file_count)
print("ham_file_count:",ham_file_count)

json_data = json.dumps(data)

model = open('nbmodel.txt', 'w')
model.write(json_data)
model.close()
