# Overlay function

from PyPDF2 import PdfFileWriter, PdfFileReader


def overlay(pdf, outfile, box, x, y, height, width):
    output_file = PdfFileWriter()
    input_file = PdfFileReader(pdf, "rb")
    logo = PdfFileReader(box, "rb")

    newfile = input_file.getPage(0)
    newpic = logo.getPage(0)
    newpic.scaleTo(width, height)

    newfile.mergeTranslatedPage(newpic, x, y, expand=False)

    output_file.addPage(newfile)

    outputStream = (open(outfile, "wb"))
    output_file.write(outputStream)
    outputStream.close()
