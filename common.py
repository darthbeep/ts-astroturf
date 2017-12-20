from nltk.corpus import stopwords
from collections import Counter
import json

def get_data():
    data = json.load(open("data.json"))
    return data

def mega(arr):
    ret = []
    for a in arr:
        filtered_words = [word for word in a.lower().split() if word not in stopwords.words('english')]
        for w in filtered_words:
            ret.append(w)
    return Counter(ret).most_common(5)

def get_vals():
    data = get_data()
    ret = {}
    for key in data:
        ret[key] = (mega(data[key]))
    return ret

def write_to_file(w):
    write = json.dumps(w)
    f = open('words.json', 'w')
    f.write(write)
#print (mega(["I wAnt tO go to ThE beach", 'parks arE cool', 'beach too']))
write_to_file(get_vals())
