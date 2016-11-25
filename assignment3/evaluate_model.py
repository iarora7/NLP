import glob, os, sys
import hw3_corpus_tool

test_dir = "test_dir"
# test_dir = "archive/test"
output_file = "output.txt"

# test_dir = sys.argv[1]
# output_file = sys.argv[2]

actual_allfiles={}
predicted_allfiles = {}

dialog_filenames = sorted(glob.glob(os.path.join(test_dir, "*.csv")))
for dialog_filename in dialog_filenames:
    file = hw3_corpus_tool.get_utterances_from_filename(dialog_filename)
    file_name = os.path.basename(dialog_filename)
    actual_tags = []
    for du in file:
        actual_tags.append(du.act_tag)
    actual_allfiles[file_name] = actual_tags


output_file = open(output_file, 'r')
output_data = output_file.read()
data = output_data.split()
file_name = ""
tag_array = []
for word in data:
    if word is None:
        print("none got")
        continue
    if "Filename" in word:
        if len(file_name) > 0:
            predicted_allfiles[file_name] = tag_array
        file_name = word[10:]
        file_name = file_name[:-1]
        tag_array = []
    else:
        tag_array.append(word)
if file_name is not None:
    predicted_allfiles[file_name] = tag_array

total=0
correct=0

for k, v in actual_allfiles.items():
    actual_tags = v
    predicted_tags = predicted_allfiles[k]
    for j in range(0, len(actual_tags)):
        total += 1
        if actual_tags[j] == predicted_tags[j]:
            correct += 1
        else:
            continue

print("correct tags:", correct)
print("total tags:", total)
print("accuracy:", (correct/total)*100 , "%")


