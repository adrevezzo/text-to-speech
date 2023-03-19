from PyPDF2 import PdfReader
import re



def read_pdf(pdf_file):
    text = ''
    with open(pdf_file, "rb") as file:
        pdf = PdfReader(file)
        for page in pdf.pages:
            raw_text = page.extract_text().split()
            joined_text = ' '.join(raw_text)
            text += joined_text
    
    return text
        



