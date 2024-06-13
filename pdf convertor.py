import os
import PyPDF2
from pdf2image import convert_from_path

def pdf_to_text(pdf_path, text_output_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text_content = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text_content += page.extractText()
        
    with open(text_output_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text_content)

def pdf_to_images(pdf_path, image_output_dir):
    images = convert_from_path(pdf_path)
    if not os.path.exists(image_output_dir):
        os.makedirs(image_output_dir)
    for i, image in enumerate(images):
        image_path = os.path.join(image_output_dir, f"page_{i+1}.jpg")
        image.save(image_path, 'JPEG')

# Example usage
pdf_path = 'example.pdf'
text_output_path = 'output.txt'
image_output_dir = 'images'

pdf_to_text(pdf_path, text_output_path)
pdf_to_images(pdf_path, image_output_dir)
