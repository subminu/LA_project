import gensim
from os import walk

file_list = []
current_path = "/aclImdb/test/neg/"
for (dirpath, dirnames, filenames) in walk(current_path):
    file_list.extend(filenames)
    break

def read_input(current_path, file_list):
    for i in range(len(file_list)):
        with open(current_path + file_list[i], encoding='utf-8') as file:
            for j, line in enumerate(file):
                yield gensim.utils.simple_preprocess(line)

document = list(read_input(current_path, file_list))
model = gensim.models.Word2Vec (document, size=50, window=10, min_count=2, workers=4)
model.train(document, total_examples=len(document), epochs=10)