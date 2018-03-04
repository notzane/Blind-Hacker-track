# Tests accuracy of Stanford Model on NFL names with no context

import re
import unidecode # requires separate install
import nltk # requires separate install
import numpy # requires separate install
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

stanford_classifier = r"C:\Users\Me\Documents\Hackathon\2018\Disrupt the District\env" \
                      "\stanford-ner-2018-02-27\classifiers\english.conll.4class.distsim.crf.ser.gz"
stanford_ner_path = r"C:\Users\Me\Documents\Hackathon\2018\Disrupt the District\env" \
                      "\stanford-ner-2018-02-27\stanford-ner.jar"
stanford_tagger = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding = "utf-8")

# only has to be run for setup, then commented out
#nltk.download()


# make names in the format First Last (vs FiRst, etc)
def makeTitle(aList):
    newList = []
    for i in aList:
        newList.append(i.title())
    return newList


# remove apostrophes within names
def noApostrophes(aList):
    newList = []
    for i in aList:
        newList.append(re.sub("\'", "", i))
    return newList

# saves time by not iterating twice
def both(aList):
    newList = []
    for i in aList:
        i = (re.sub("\'", "", i))
        newList.append(i.capitalize())
    return newList

def recognizeName(fileName):
    lineList = []
    names = 0
    # removes diacritics
    with open(fileName, 'rt', encoding='utf-8') as fn:
        text = fn.read()
        tags = stanford_tagger.tag(word_tokenize(text))
        while len(tags) > 0:
            if tags[0][1] == "PERSON" or tags[1][1] == "PERSON":
                names += 1
            del tags[0]
            del tags[0]
        return names

recognizedNames = recognizeName("testplayers.txt")
print("There were " + str(recognizedNames) + " names recognized, or " + str(100 * (recognizedNames / 21861)) + " percent.")
