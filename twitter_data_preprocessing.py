import csv
import re
import string

import matplotlib.pyplot as plt
import nltk
import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from spellchecker import SpellChecker
from textblob import TextBlob

twitter = pd.read_csv(
    r"C:\Users\pawan_300\Desktop\Project work\ml files\ml project\tweets.csv"
)

print(twitter.head(5))

# Cleaning


def stopword():
    stop = stopwords.words("english")
    twitter["Text"] = twitter["Text"].apply(
        lambda x: " ".join([word for word in x.split() if word not in (stop)])
    )  # Stopword removal


def remove():
    twitter["Text"] = twitter["Text"].apply(
        lambda x: re.sub(r"http\S+", "", x)
    )  # for url
    twitter["Text"] = twitter["Text"].apply(
        lambda x: re.sub(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", "", x)
    )  # for email
    twitter["Text"] = twitter["Text"].apply(
        lambda x: re.sub("@[^\s]+", "", x)
    )  # for username
    twitter["Text"] = twitter["Text"].apply(
        lambda x: re.sub("#[^\s]+", "", x)
    )  # for trending # words
    twitter["Text"] = twitter["Text"].apply(lambda x: re.sub("\$\w*", "", x))


stopword()
remove()

punct_num = '''!()-àÂ[]{};:\n,<>./?@#%^"&\*_~0123456789=\x92\x92\x96\x85+|'"'''  # for punctuation


def punctuation(x):
    no_punct = ""
    for char in x:
        if char not in punct_num:
            no_punct = no_punct + char
    return no_punct


twitter["Text"] = twitter["Text"].apply(lambda x: punctuation(x))

fileName = r"C:\Users\pawan_300\Desktop\Project work\ml files\ml project\slang.txt"
accessMode = "r"


def slang_translator(user_string):
    user_string = user_string.split(" ")
    j = 0
    for _str in user_string:
        with open(fileName, accessMode) as myCSVfile:
            dataFromFile = csv.reader(myCSVfile, delimiter="=")
            _str = re.sub("[^a-zA-Z0-9-_.]", "", _str)
            for row in dataFromFile:
                if _str.upper() == row[0]:
                    user_string[j] = row[1]
            myCSVfile.close()
        j = j + 1
    return " ".join(user_string)


twitter["Text"] = twitter["Text"].apply(lambda x: slang_translator(x))

spell = SpellChecker()


def spellcheck(x):
    correct = {}
    wrong = spell.unknown(x.split())
    for t in wrong:
        correct[t] = spell.correction(t)
    for t in correct.keys():
        x = re.sub(t, correct[t], x, flags=re.IGNORECASE)
    return x


twitter["Text"] = twitter["Text"].apply(
    lambda x: spellcheck(x)
)  # this will take some time

# Polarity


def polarity():
    pole = []
    t = []
    for line in twitter["Text"]:
        temp = TextBlob(line).sentiment.polarity
        t.append(temp)
        if temp > 0:
            pole.append("positive")
        elif temp < 0:
            pole.append("negative")
        else:
            pole.append("neutral")
    return (pole, t)


pole, temp = polarity()
twitter["Sentiment"] = pole
twitter["Sentiment_score"] = temp

print("Distribution :")
plt.hist(pole, histtype="bar", align="mid")
