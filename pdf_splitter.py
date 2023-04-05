import os
import PyPDF2
from datetime import datetime

input_path = input("Enter path to PDF: ")
output_path = input("Enter Output Path-Folder: ")

output_folder = os.path.join(output_path, 'splitter')

with open(input_path, 'rb') as input_file:
    pdf_reader = PyPDF2.PdfReader(input_file)

    for page_num, page in enumerate(pdf_reader.pages):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(page)

        # Use f-string to generate output filename
        output_filename = f"{output_folder}_{page_num + 1}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f"Saved page {page_num + 1} to {output_filename}")

print("Done")
