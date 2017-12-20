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
from sklearn.manifold import TSNE

with open('words.json') as json_data:
    data = json.load(json_data)
    #print(d)

clean_data = []

# cleaning data: removing punctuation, uppercase, stopwords, convert to list of words
for key in data: #list of dict values (comments)
    for element in data[key]:
        if type(element) != int:
            clean_data.append(element)

print clean_data

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
#print model

#print model.most_similar(['columbia'])

# kmeans cluster

def tsne_plot(model):
    #"Creates and TSNE model and plots it"
    labels = []
    tokens = []

    for word in model.wv.vocab:
        tokens.append(model[word])
        labels.append(word)
    #print (labels)
    #print (tokens)

    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])

    plt.figure(figsize=(16, 16))
    for i in range(len(x)):
        plt.scatter(x[i],y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()

tsne_plot(model)
