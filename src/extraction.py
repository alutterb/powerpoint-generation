'''
Handles the extraction of raw text and images from the uploaded documents
Currently will support pdf and docx files
'''
import pdfplumber
from PIL import Image
import os
import pickle
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

# each class will be tied to a specific document that the user uploaded in gui.py
class Extractor:
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

    def process_page_helper(self, page):
        # use logic from pdfplumber if pdf
        if self.file_ext == '.pdf':
            try:
                page_number = page.page_number
                text = page.extract_text() if page.extract_text() else ""
                return page_number, text
            except Exception as e:
                print(f"Error processing page: {e}")
                return -1, ""
        if self.file_ext == '.docx':
            pass
        return False

    def extract_from_pdf(self):
        info_dict = {'PAGE' : [], 'TEXT' : []}
        with pdfplumber.open(self.file_path) as pdf:
            # Use ThreadPoolExecutor to process pages in parallel
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(self.process_page_helper, page) for page in pdf.pages]

                for future in concurrent.futures.as_completed(futures):
                    page_num, text = future.result()
                    info_dict['PAGE'].append(page_num)
                    info_dict['TEXT'].append(text)
        print("Information from pdf successfully extracted.")
        return info_dict


    def extract_text_from_docx(self):
        pass
