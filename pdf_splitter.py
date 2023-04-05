import os
import PyPDF2
from datetime import datetime

input_path = input("Enter path to PDF: ")
output_path = input("Enter Output Path-Folder: ")
if output_path[-1] != '\\':
    output_path += '\\splitter'
else:
    output_path += 'splitter'

with open(input_path, 'rb') as input_file:
    pdf_reader = PyPDF2.PdfReader(input_file)

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{output_path}_{page_num + 1}_{timestamp}.pdf"

        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f"Saved page {page_num + 1} to {output_filename}")

print("Done")
