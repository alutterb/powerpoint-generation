'''
This file will use tkinker to create a simple GUI for uploading documents
and specifying additional details for how the powerpoint should be generated.
'''

import tkinter as tk
from tkinter import filedialog

def upload_action():
    # Code to handle file upload
    pass

def start_processing():
    # Code to initiate the processing pipeline
    pass

root = tk.Tk()
root.title("Presentation Generator")

upload_btn = tk.Button(root, text="Upload File", command=upload_action)
upload_btn.pack()

# Add inputs for hyperparameters
# Example: number of slides
num_slides_label = tk.Label(root, text="Number of Slides:")
num_slides_label.pack()
num_slides_entry = tk.Entry(root)
num_slides_entry.pack()

# More hyperparameter inputs can be added here

# Button to start processing
start_btn = tk.Button(root, text="Start Processing", command=start_processing)
start_btn.pack(pady=20)

root.mainloop()
