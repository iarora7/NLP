import re

def fileopen(input):
    classfiedSpam=0
    classifiedHam=0
    actualSpam=0
    actualHam=0
    correctClassifiedSpam=0
    correctClassifieHam=0
    f=open(input,'r')
    l=f.read().split('\n')
    for line in l:
        if line:
            print(line.split()[1])
            if(line.split()[0]=='HAM'):
                classifiedHam+=1
            else:
                classfiedSpam+=1
            if re.search('.*spam.*', str(line.split()[1])):
                actualSpam+=1
            else:
                actualHam+=1
            if(line.split()[0]=='HAM' and re.search('.*ham.*', str(line.split()[1]))):
                 correctClassifieHam+=1
            if(line.split()[0]=='SPAM' and re.search('.*spam.*', str(line.split()[1]))):
                correctClassifiedSpam+=1
    print(classfiedSpam,' ',correctClassifiedSpam)
    ps=correctClassifiedSpam/classfiedSpam
    ph=correctClassifieHam/classifiedHam
    rs=correctClassifiedSpam/actualSpam
    rh=correctClassifieHam/actualHam
    print("Precision Spam=",ps)
    print("Precision Ham=", ph)
    print("Recall Spam=",rs)
    print("Recall Ham=",rh)
    print("F1 Spam=",2*ps*rs/(ps+rs))
    print("F1 Ham=",2*rh*ph/(rh+ph))


fileopen("/Users/isha/USC/sem3/NLP/assignments/NLP/assignment2/per_output.txt")
