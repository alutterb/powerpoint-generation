'''
Uses tkinker to create a simple GUI for uploading documents
and specify additional details for how the powerpoint should be generated.
'''

import tkinter as tk
from tkinter import filedialog
from extraction import Extractor

class PresentationGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Presentation Generator")

        # Initialize the list to store file paths
        self.uploaded_files = []

        # Create and place the upload button
        self.upload_btn = tk.Button(self.root, text="Upload Files", command=self.upload_action)
        self.upload_btn.pack(pady=10)

        # Create and place the start processing button
        self.start_btn = tk.Button(self.root, text="Start Processing", command=self.start_processing)
        self.start_btn.pack(pady=10)


    def upload_action(self):
        # Open file dialog and allow user to select files
        file_paths = filedialog.askopenfilenames()  # Returns a tuple of file paths
        for file_path in file_paths:
            if file_path:
                self.uploaded_files.append(file_path)
                print(f"Uploaded: {file_path}")  # Just for confirmation

    def start_processing(self):
        for file in self.uploaded_files:
            res = Extractor(file).extract_data()
            break


# Create the main window
root = tk.Tk()

# Create an instance of the Application
app = PresentationGeneratorApp(root)

# Start the main loop
root.mainloop()
