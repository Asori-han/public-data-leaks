import re
import os
from PyPDF2 import PdfReader

# Extract all DNIs from pdf
def get_dni(reader):
    dni_list = []
    for i, page in enumerate(reader.pages):
        dnis = re.findall(r'[0-9*]{8}[a-zA-Z*]', page.extract_text())
        dni_list.extend(dnis)

    return dni_list

# List PDFs in path
def pdf_list(path):
    files = os.listdir(path)
    pdfs = [file for file in files if file.endswith('.pdf')]
    return pdfs

# Writes each item of list on file
def write_list(filename, list):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in list:
            file.write(i + '\n')

def extract_dni_from_pdf_folder(path):
    pdfs = pdf_list(path)
    for pdf in pdfs:
        try:
            reader = PdfReader(f"{path}/{pdf}")
            dni_list = get_dni(reader)
            write_list(f"{path}/{pdf[:-3]}txt", dni_list)
        except:
            print(f"Error on file {pdf}")

extract_dni_from_pdf_folder('docs/downloads')
