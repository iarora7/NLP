import json
import os
import math
import re
import sys

# path = r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment1/files/dev"
# path = r"/Users/isha/USC/sem3/NLP/assignments/NLP/assignment1/Sample/dev"
path = sys.argv[1]

ham_dict = {}
spam_dict = {}
spam_file_count = 0
ham_file_count = 0
spam_wc = 0
ham_wc = 0
vocab_wc = 0

stop_words = []
stop_file = open('stopwords.txt','r')
for word in stop_file:
    word = word.strip()
    stop_words.append(word)

output_file = open('nboutput.txt', 'w')

model_file = open("nbmodel.txt", 'r', encoding='latin1')
file_data = model_file.read()
file_data = json.loads(file_data)
for k in file_data:
    if (k == "spam_file_count"):
        spam_file_count = file_data[k]
    if (k == "ham_file_count"):
        ham_file_count = file_data[k]
    if (k == "spam_wc"):
        spam_wc = file_data[k]
    if (k == "ham_wc"):
        ham_wc = file_data[k]
    if (k == "vocab_wc"):
        vocab_wc = file_data[k]
    if (k == "ham_dict"):
        ham_dict = file_data[k]
    if (k == "spam_dict"):
        spam_dict = file_data[k]

total_file_count = spam_file_count + ham_file_count
prob_spam = spam_file_count/total_file_count
prob_ham = ham_file_count/total_file_count

print(prob_spam)
print(prob_ham)

for dirName, subdirList, fileList in os.walk(path):
    for fname in fileList:
        fpath = os.path.join(dirName, fname)
        # if "DS_Store" in fpath:
        #     break
        my_file = open(fpath, 'r', encoding='latin1')
        test_data = my_file.read().split()
        word_dict = {}
        p_word_spam = 1
        p_word_ham = 1
        word_count = 0
        for word in test_data:
            word = word.lower()
            word = re.sub("[^a-zA-z0-9]", "", word)
            if word in stop_words:
                break
            else:
                if word in word_dict:
                    word_dict[word][0] += 1
                else:
                    word_count = 1
                    if word in spam_dict:
                        p_word_spam = (spam_dict[word] + 1) / (spam_wc + vocab_wc)
                    elif word in ham_dict:
                        p_word_spam = 1 / (spam_wc + vocab_wc)

                    if word in ham_dict:
                        p_word_ham = (ham_dict[word] + 1) / (ham_wc + vocab_wc)
                    elif word in spam_dict:
                        p_word_ham = 1 / (ham_wc + vocab_wc)

                    word_dict[word] = [word_count, math.log(p_word_spam), math.log(p_word_ham)]
        log_p_doc_spam = 0
        log_p_doc_ham = 0
        for key in word_dict:
            log_p_doc_spam += (word_dict[key][0] * word_dict[key][1])
            log_p_doc_ham += (word_dict[key][0] * word_dict[key][2])

        log_p_spam = math.log(prob_spam)
        log_p_ham = math.log(prob_ham)
        p_spam_doc = log_p_spam + log_p_doc_spam
        p_ham_doc = log_p_ham + log_p_doc_ham
        if(p_spam_doc > p_ham_doc):
            output_file.write("SPAM " + fpath + "\n")
        else:
            output_file.write("HAM " + fpath + "\n")



