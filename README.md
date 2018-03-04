# **ResumeBias**
## Blind Web App
### Disrupt the District 2018

# Demo
[resumeblind.com](http://resumeblind.com)


# Purpose
To support equality and diversity in the hiring process.

## Why
White male applicants recieve up to 36% more callbacks than their peers based on their names.

## What
Blind strips the name off of the resume to reduce racial or gender bias during the first round of hiring.

## How
Blind uses natural laguage processing to identify the name and email to generate a new resume.

# Usage
Upload your resume in PDF format on the demo website. Choose how much information you want to remove by clicking the buttons below the submission box. The new PDF will automatically download onto your computer.

# Dependencies
Python 3.6+

nltk (Stanford NLP module optional)

numpy

pdfminer.six

PyPDF2

unidecode

### Note:
need to run nltk.dowload() and choose book before running entire program

# Sources Used:

## NLTK
Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O'Reilly Media Inc. (nltk.org)

## Email Regex
http://www.regular-expressions.info/email.html

## Stanford NLP with NLTK
https://blog.manash.me/configuring-stanford-parser-and-stanford-ner-tagger-with-nltk-in-python-on-windows-f685483c374a

## NFL Players Dataset
https://raw.githubusercontent.com/theliamcrawford/6-Degrees-of-NFL-Players/master/names.txt
