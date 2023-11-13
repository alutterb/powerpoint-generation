'''
Handles the extraction of raw text and images from the uploaded documents
Currently will support pdf and docx files
'''
import pdfplumber
import pickle
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

# each class will be tied to a specific document that the user uploaded in gui.py
class TextExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_ext = ''

    def extract_text(self):
        # Determine file type and call the appropriate extraction method
        if self.file_path.endswith('.pdf'):
            self.file_ext = '.pdf'
            return self.extract_from_pdf()
        elif self.file_path.endswith('.docx'):
            self.file_ext = '.docx'
            return self.extract_from_docx()
        else:
            raise ValueError("Unsupported file format - only supported formats are pdf or docx")

    def process_page(self, page):
        # use logic from pdfplumber if pdf
        if self.file_ext == '.pdf':
            try:
                return page.extract_text() if page.extract_text() else ""
            except Exception as e:
                print(f"Error processing page: {e}")
                return ""
        if self.file_ext == '.docx':
            pass
        return False

    def extract_from_pdf(self):
        extracted_texts = []
        with pdfplumber.open(self.file_path) as pdf:
            # Use ThreadPoolExecutor to process pages in parallel
            with ThreadPoolExecutor() as executor:
                results = executor.map(self.process_page, pdf.pages)
            extracted_texts = list(results)
        
        # Combine texts from all pages
        return "\n".join(extracted_texts)


    def extract_from_docx(self):
        pass

    
