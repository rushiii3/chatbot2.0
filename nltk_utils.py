import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np
stemmer = PorterStemmer()
#nltk.download('punkt')
def tokenize(sentence):
    return nltk.word_tokenize(sentence)
def stem(word):
    return stemmer.stem(word.lower())
def bag_of_words(tokenized_sentence,words):
    stemed = [stem(words) for words in tokenized_sentence]
    bag = np.zeros(len(words),dtype=np.float32)
    for idx,w in enumerate(words):
        if( w in stemed ):
            bag[idx] = 1
    return bag