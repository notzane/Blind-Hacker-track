#help from pdfminer docs and https://stackoverflow.com/questions/25248140/how-does-one-obtain-the-location-of-text-in-a-pdf-with-pdfminer

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure
from pdfminer.pdfdevice import PDFDevice


def find_corners(layout, name):
    """Function to parse the layout tree."""
    for component in layout:
        if isinstance(component, LTTextBox) or isinstance(component, LTTextLine):
            if(name.lower() in component.get_text().lower()):
                return(component.bbox) # (x0,y0,x1,y1)
        elif isinstance(component, LTFigure): #needs to dig a level deeper to get to a textboxline
            parse_layout(component)
    print("error:could not find name")

def find_position(filename, name):
    """Funtion to find position from name and file"""
    with open(filename, "rb") as fp: # try to open input file (r-read, b- binary)
        # setup taken from example code in docs
        parser = PDFParser(fp) # Create a PDF document object that stores the document structure.
        document = PDFDocument(parser) # initialize document
        rsrcmgr = PDFResourceManager() # Create a PDF resource manager object that stores shared resources.
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams) # Create the PDF device object.
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()
            return(find_corners(layout, name))

def find_name(filename, name):
    """Accepts filename and a name and returns (x,y,h,w)"""
    corners = find_position(filename, name)
    return (corners[0], corners[1], corners[3] - corners[1], corners[2] - corners[0])

#print(find_pos_size("resume.pdf", "Zane"))
