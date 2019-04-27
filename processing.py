import os
import re
dict = {}
review_list =[]
id = 0
re_extract = re.compile('\d+_(\d+)') #score is mapped by ()

def evaluation(score):
    if int(score[0]) > 5:
        return 'pos'
    else:
        return 'neg'

def replace(text):
    return text.replace('<br />',"")

for senti in ['neg','pos']:
    directory = f"C:\\Users\\submi\\OneDrive\\바탕 화면\\aclImdb\\test\\{senti}"
    review_list = os.listdir(directory)

    for file in review_list:
        re_score = re_extract.findall(file)
        directory = f"C:\\Users\\submi\\OneDrive\\바탕 화면\\aclImdb\\test\\{senti}\\{file}"
        with open(directory,'rt') as f:
            try:
                review = f.read()
            except UnicodeDecodeError:
                print(id)
                id -= 1
        review = replace(review)
        value = evaluation(re_score)
        dict[id] = {'value':value, 'score':int(re_score[0]), 'text':review}
        id += 1
with open('C:\\Users\\submi\\PycharmProjects\\makeDataset\\dataset.txt','wt') as f:
    print(dict, file=f, end = '\n')