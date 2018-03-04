import recognizeName
import recognizeEmails
import overplay
import find_name
import extract_text



def unbias(filename, outfile, email=False):
    filenametxt = "resume.txt"
    extract_text.extract(filename, filenametxt, "text")
    name = recognizeName.recognizeName(filenametxt)
    pos_size = find_name.find_name(filename, name)
    overplay.overlay(filename, outfile, "bigredbox.pdf", *pos_size)

    if(email):
        emails = recognizeEmails.recognizeEmails(filenametxt)
        print(emails)
        for e in emails:
            pos_size = find_name.find_name(filename, e)
            overplay.overlay(outfile, outfile, "bigredbox.pdf", *pos_size)
