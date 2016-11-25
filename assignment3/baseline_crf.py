import pycrfsuite
import time
import glob, os, sys
import hw3_corpus_tool

input_dir = "input_dir"
test_dir = "test_dir"
# input_dir = "archive/train"
# test_dir = "archive/test"
opfile = "output.txt"

input_dir = sys.argv[1]
test_dir = sys.argv[2]
opfile = sys.argv[3]

output_file = open(opfile, 'w')

start_time = time.time()
train_data = hw3_corpus_tool.get_data(input_dir)
x_train = []
y_train=[]

for file in list(train_data):
    sp = file[0].speaker
    first = True
    for du in file:
        utt=[]
        token=[]
        pos=[]
        y_train.append(du.act_tag)
        if first == True:
            first = False
            beg = 1
        else:
            beg = 0
        speaker = 1 if du.speaker == sp else 0
        utt = [str(beg), str(speaker)]
        if du.pos is None:
            x_train.append(utt)
        else:
            for postag in du.pos:
                mytoken = "TOKEN_" + postag.token
                token.append(mytoken)
                mypos = "POS_" + postag.pos
                pos.append(mypos)
            utt = utt + token + pos
            x_train.append(utt)

print("xtrain len", len(x_train))
print("ytrain len", len(y_train))

trainer = pycrfsuite.Trainer(verbose=False)
trainer.append(x_train, y_train)

trainer.set_params({
    'max_iterations': 100,  # stop earlier
})
trainer.params()
trainer.train('conll2002-esp.crfsuite')
print("Training Done")

# Test data
actual_allfiles = []
predicted_allfiles = []
tagger = pycrfsuite.Tagger()
tagger.open('conll2002-esp.crfsuite')

# test_data = hw3_corpus_tool.get_data(test_dir)

dialog_filenames = sorted(glob.glob(os.path.join(test_dir, "*.csv")))
for dialog_filename in dialog_filenames:
    file = hw3_corpus_tool.get_utterances_from_filename(dialog_filename)
    file_name = os.path.basename(dialog_filename)

    feature_list = []
    actual_tags = []
    sp = file[0].speaker
    first = True
    for du in file:
        utt=[]
        token=[]
        pos=[]
        actual_tags.append(du.act_tag)

        if first:
            first = False
            beg = 1
        else:
            beg = 0
        speaker = 1 if du.speaker == sp else 0
        utt = [str(beg), str(speaker)]
        if du.pos is None:
            feature_list.append(utt)
        else:
            for postag in du.pos:
                mytoken = "TOKEN_" + postag.token
                token.append(mytoken)
                mypos = "POS_" + postag.pos
                pos.append(mypos)
            utt = utt + token + pos
            feature_list.append(utt)
    predicted_tags = tagger.tag(feature_list)

    output_file.write('Filename="' + file_name + '"\n')
    output_file.write("\n".join(predicted_tags))
    output_file.write("\n\n")

print("Tested for", len(dialog_filenames), "files")
print("---baseline.crf %s seconds ---" % (time.time() - start_time))