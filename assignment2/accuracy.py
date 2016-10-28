import sys

# path = sys.argv[1]
path = 'per_output.txt'
# path = '/Users/arorai/USC/sem3/nlp/assignments/NLP/assignment2/per_output.txt'

labelSpam=0
labelHam=0
actaulSpam=0
actualHam=0
correctSpam=0
correctHam=0
totalFiles=0

outputFile = open(path, 'r')
fileLines = outputFile.read().split('\n')
for l in fileLines:
    if l:
        totalFiles += 1
        parts = l.split()
        if (parts[0].lower() == "spam"):
            labelSpam += 1
        elif (parts[0].lower() == "ham"):
            labelHam += 1

        if ("spam" in parts[1].lower()):
            actaulSpam += 1
        elif ("ham" in parts[1].lower()):
            actualHam += 1

        if (parts[0].lower() == "spam" and "spam" in parts[1].lower()):
            correctSpam += 1
        elif (parts[0].lower() == "ham" and "ham" in parts[1].lower()):
            correctHam += 1

pspam = correctSpam/labelSpam
pham = correctHam/labelHam
rspam = correctSpam/actaulSpam
rham = correctHam/actualHam
fspam = (2 * pspam * rspam)/(pspam + rspam)
fham = (2 * pham * rham)/(pham + rham)

weighted_average = ((actaulSpam * fspam)/totalFiles) + ((actualHam * fham)/totalFiles)
print("Precision Spam: ", pspam)
print("Precision Ham:  ", pham)
print("Recall Spam:    ", rspam)
print("Recall Ham:     ", rham)
print("F1 Spam:        ", fspam)
print("F1 Ham:         ", fham)
print("weighted_average", weighted_average)


