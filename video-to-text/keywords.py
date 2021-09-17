from nltk import tokenize
from operator import itemgetter
import math

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))

doc = "hai to talk about binary heap Data Structure Data Structure is used to implement heap sort a popular sorting algorithm it is also used to implement Priority Queue in fact the main application of binary bits tourist implementation of priority queues are useful in many standard algorithms like this for shortest path algorithm algorithm Huffman coding in any situation and these items are provided is for example a doctor's Q there are multiple patients want to visit a single doctor every patient is assigned a Priority and doctor always visits the highest priority person next and was the highest priority person is visited next highest quality purse is visited next so there are many many practical situations where we need Priority Queue and most of the time Priority Queue is implemented using heap Data Structure to assigned to the people you assign the numbers such a way that the lowest number assigned to a person is the highest priority and this is what we call the lowest value"

total_words = doc.split()
total_word_length = len(total_words)
print(total_word_length)

total_sentences = tokenize.sent_tokenize(doc)
total_sent_len = len(total_sentences)
print(total_sent_len)

tf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in tf_score:
            tf_score[each_word] += 1
        else:
            tf_score[each_word] = 1

# Dividing by total_word_length for each dictionary element
tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())
print(tf_score)

def check_sent(word, sentences): 
    final = [all([w in x for w in word]) for x in sentences] 
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))

idf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in idf_score:
            idf_score[each_word] = check_sent(each_word, total_sentences)
        else:
            idf_score[each_word] = 1

# Performing a log and divide
idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())

print(idf_score)

tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
print(tf_idf_score)

def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
    return result

print(get_top_n(tf_idf_score, 5))