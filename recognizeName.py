# returns the first name recognized from an input

import re
import unidecode # requires separate install
import nltk # requires separate install
import numpy # requires separate install
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

stanford_classifier = r"StanfordParser/stanford-ner-2018-02-27/classifiers/english.conll.4class.distsim.crf.ser.gz"
stanford_ner_path = r"StanfordParser/stanford-ner-2018-02-27/stanford-ner.jar"
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
        newList.append((re.sub("\'", "", i)).title())
    return newList

def recognizeName(fileName):
    lineList = []
    nameList = []
    recognizeList = []
    # removes diacritics
    with open(fileName, 'rt', encoding='utf-8') as fn:
        text = fn.read()
        text = unidecode.unidecode(text)
        tags = stanford_tagger.tag(word_tokenize(text))
        name = [tag[0] for tag in tags if tag[1] == "PERSON"]
        return name[0]

'''
This is for just using nltk without the Stanford model. It's faster but it doesn't work as well.
def recognize(aList):
    names = []
    for i in aList:
        tokens = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(tokens)
        for entity in nltk.chunk.ne_chunk(tagged):
            if type(entity) == nltk.tree.Tree:
                if entity.label() == 'PERSON':
                    names.append(i)
                    break
    return names

# returns first name found
# file must be in utf-8 if it has diacritics
def recognizeName(fileName):
    lineList = []
    nameList = []
    recognizeList = []
    # removes diacritics
    with open(fileName, 'rt', encoding='utf-8') as fn:
        for line in fn:
            line = unidecode.unidecode(line)
            lineList.append(line.strip())
    nameList = both(lineList)
    print(nameList)
    recognizeList = recognize(nameList)
    print(recognizeList)
    return recognizeList[0]
'''
