import recognizeName
import recognizeEmails
import overplay
import find_name
import extract_text

filenamepdf = "sample_resumes/sample2.pdf"
filenametxt = "resume.txt"

extract_text.extract(filenamepdf, filenametxt, "text")

name = recognizeName.recognizeName(filenametxt)
print(name)
pos_size = find_name.find_name(filenamepdf, name)
overplay.overlay(filenamepdf, "bigredbox.pdf", *pos_size)

emails = recognizeEmails.recognizeEmails(filenametxt)
print(emails)
for e in emails:
    pos_size = find_name.find_name(filenamepdf, e)
    overplay.overlay("resume_unbiased.pdf", "bigredbox.pdf", *pos_size)
