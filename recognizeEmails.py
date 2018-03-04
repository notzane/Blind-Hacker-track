# uses regex to find all emails on the page
import re


def recognizeEmails(fileName):
    emailList = []
    with open(fileName, 'r', encoding='utf-8') as fn:
        text = fn.read()
    emailList = re.findall(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", text, re.I)
    return emailList


