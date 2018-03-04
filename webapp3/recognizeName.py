# returns the first name recognized from an input

import re
import unidecode # requires separate install
import nltk # requires separate install
import numpy # requires separate install

nltk.data.path = ['nltk_data']

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
    recognizeList = recognize(nameList)
    return recognizeList[0]
