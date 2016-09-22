
spam_positive=0
spam_negative=0
ham_positive=0
ham_negative=0

model_file = open("nboutput.txt", 'r', encoding='latin1')
file_data = model_file.read()
lines = file_data.splitlines()
for file in lines:
    words = file.split()
    if words[0] == "Spam":
        if "spam" in words[1]:
            spam_positive += 1
        else:
            spam_negative += 1
    if words[0] == "Ham":
        if "ham" in words[1]:
            ham_positive += 1
        else:
            ham_negative += 1


total = spam_negative+spam_positive+ham_negative+ham_positive
print("spam_negative:",spam_negative)
print("spam_positive:",spam_positive)
print("ham_negative:",ham_negative)
print("ham_positive:",ham_positive)

print((spam_positive+ham_positive)/total)