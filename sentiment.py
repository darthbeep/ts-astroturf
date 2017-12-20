import nltk
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
import gensim
from gensim import logging, corpora
import logging
import string
import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

#from sklearn.cluster import MiniBatchKMeans as kmeans

#data = ["Dear Chairman Pai, I am concerned about internet regulations. I suggest the commission to repeal Tom Wheeler's decision to control the Internet. Internet users, rather than so-called experts, should be empowered to enjoy whichever applications we want. Tom Wheeler's decision to control the Internet is a exploitation of the open Internet. It ended a pro-consumer policy that functioned very, very successfully for a long time with bipartisan support.", "Chairman Pai: In the matter of the FCC's so-called Open Internet order. I want to recommend you to overturn The previous administration's decision to take over broadband. Internet users, not Washington, should be free to purchase the applications we choose. The previous administration's decision to take over broadband is a perversion of net neutrality. It ended a market-based policy that worked very, very successfully for a long time with broad bipartisan support."]

with open('data.json') as json_data:
    data = json.load(json_data)
    #print(d)

clean_data = []

# cleaning data: removing punctuation, uppercase, stopwords, convert to list of words
for key in data: #list of dict values (comments)
    clean_data.append(data[key])

clean_data2 = []
stop = set(stopwords.words('english'))

def process(comment):
    comment = comment.lower() # convert to lowercase
    tokenizer = RegexpTokenizer(r'\w+') # remove punctuation
    tokens = tokenizer.tokenize(comment) # convert to list of tokens
    data = [word for word in tokens if word not in stop] # goes through comment and removes stopwords and adds to a list
    return data

for element in clean_data:
    for word in element:
        clean_data2.append(process(word))

# convert words to vector

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = gensim.models.Word2Vec(clean_data2, min_count = 1)
model.train(clean_data2, total_examples=model.corpus_count,epochs=model.iter)
print model
print model.most_similar(['columbia'])

# kmeans cluster
