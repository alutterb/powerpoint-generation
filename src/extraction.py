'''
Handles the extraction of raw text and images from the uploaded documents
Currently will support pdf and docx files
'''
import pdfplumber
from pytesseract import image_to_string
import docx

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

import logging
import datetime 
# each class will be tied to a specific document that the user uploaded in gui.py
class Extractor:
    # datetime timestamp for logging
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")

    # set up logging
    logger = logging.getLogger("Extractor")
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(f'logs/pdf_processing_errors_{timestamp}.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_ext = ''

    def extract_data(self):
        # Determine file type and call the appropriate extraction method
        if self.file_path.endswith('.pdf'):
            self.file_ext = '.pdf'
            return self.extract_from_pdf()
        elif self.file_path.endswith('.docx'):
            self.file_ext = '.docx'
            return self.extract_from_docx()
        else:
            raise ValueError("Unsupported file format - only supported formats are pdf or docx")

    def extract_from_pdf(self):
        info_dict = {'PAGE': [], 'TEXT': []}
        # get number of pages in pdf
        with pdfplumber.open(self.file_path) as pdf:
            #page_numbers = range(len(pdf.pages))
            for i, page in enumerate(pdf.pages):
                info_dict['PAGE'].append(i)
                info_dict['TEXT'].append(page.extract_text())

        print("Information from pdf successfully extracted.")
        return info_dict

    def extract_from_docx(self):
        try:
            doc = docx.Document(self.file_path)
        except Exception as e:
            self.logger.error(f"Error opening docx file: {e}")
            return []
        
        info_dict = {'PARAGRAPH' : [], 'TEXT' : []}
        for i, para in enumerate(doc.paragraphs):
            info_dict['PARAGRAPH'].append(i)
            info_dict['TEXT'].append(para.text)
        
        return info_dict

