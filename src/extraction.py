'''
Handles the extraction of raw text and images from the uploaded documents
Currently will support pdf and docx files
'''
import pdfplumber
from pytesseract import image_to_string
import docx

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

    def extract_from_pdf(self):
        info_dict = {'PAGE': [], 'TEXT': []}
        # loop through and grab page number and text from each page
        with pdfplumber.open(self.file_path) as pdf:
            for page in pdf.pages:
                page_number = page.page_number
                text = page.extract_text()
                # if no text layers, use ocr scanner
                if not text:
                    text = image_to_string(page.to_image())
                info_dict['PAGE'].append(page_number)
                info_dict['TEXT'].append(text)
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

