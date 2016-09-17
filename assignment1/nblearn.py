import os;

path = r"/Users/isha/USC/sem3/nlp/ass1/files"

vocab = set()
hamdic = {}
spamdic = {}

def readFile(fpath, labeldic):
    myfile = open(fpath, 'r', encoding='utf-8', errors='ignore')
    filedata = myfile.read().split()
    for word in filedata:
        vocab.add(word.lower())
        if word in labeldic:
            labeldic[word] += 1
        else:
            labeldic[word] = 1


for dirName, subdirList, fileList in os.walk(path):
    for fname in fileList:
        fpath = os.path.join(dirName, fname)
        if "ham" in fpath:
            labeldic = hamdic
        else:
            labeldic = spamdic
        readFile(fpath, labeldic)



# Printing HamDic, SpamDic
# for key in hamdic:
#     print(key, hamdic[key])
# print("--------------------SpamDic:")
# for key in spamdic:
#     print(key, spamdic[key])

print("len of vocab:",len(vocab))
print("len of spamdic:",len(spamdic))
print("len of hamdic:",len(hamdic))