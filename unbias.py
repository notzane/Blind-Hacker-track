import recognizeName
import overplay
import find_name
import extract_text



def unbias(filename):
    filenametxt = "resume.txt"
    extract_text.extract(filename, filenametxt, "text")
    name = recognizeName.recognizeName(filenametxt)
    pos_size = find_name.find_name(filename, name)
    overplay.overlay(filenamepdf, "bigredbox.pdf", *pos_size)
