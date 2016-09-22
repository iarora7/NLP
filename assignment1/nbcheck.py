
dev_spam_file =3675
dev_ham_file =1500
pre_spam_path_label = 0
pre_spam_count = 0
g = open('nboutput.txt', 'r')
lines = g.readlines()
for line in lines:
    line = line.split(" ")
    if line[0] == "SPAM" and "spam.txt" in line[1]:
        pre_spam_path_label = pre_spam_path_label + 1
    if line[0] == "SPAM":
        pre_spam_count = pre_spam_count + 1
g.close()
precision_spam = (pre_spam_path_label / pre_spam_count)

print(precision_spam, " Precision SPAM")

######### Pricision count for HAM
pre_ham_path_label = 0
pre_ham_count = 0
g = open('nboutput.txt', 'r')
lines = g.readlines()
for line in lines:
    line = line.split()
    if line[0] == "HAM" and "ham.txt" in line[1]:
        pre_ham_path_label = pre_ham_path_label + 1
    if line[0] == "HAM":
        pre_ham_count = pre_ham_count + 1

precision_ham = (pre_ham_path_label / pre_ham_count)
g.close()
print(precision_ham, " Precision HAM")

######### Recall of SPAM
pre_spam_path_label = 0
g = open('nboutput.txt', 'r')
lines = g.readlines()
for line in lines:
    line = line.split()
    if line[0] == "SPAM" and "spam.txt" in line[1]:
        pre_spam_path_label = pre_spam_path_label + 1

recall_spam = (pre_spam_path_label / dev_spam_file)
g.close()
print(recall_spam, "Recall SPAM")

# ######### Recall of HAM
pre_ham_path_label = 0
g = open('nboutput.txt', 'r')
lines = g.readlines()
for line in lines:
    line = line.split()
    if line[0] == "HAM" and "ham.txt" in line[1]:
        pre_ham_path_label = pre_ham_path_label + 1

recall_ham = (pre_ham_path_label / dev_ham_file)
g.close()
print(recall_ham, "Recall HAM")

########## Evaluation for SPAM
F_SPAM = ((2 * precision_spam * recall_spam) / (precision_spam + recall_spam))
F_HAM = ((2 * precision_ham * recall_ham) / (precision_ham + recall_ham))

print(F_SPAM, "F1 SPAM")
print(F_HAM, "F1 HAM")