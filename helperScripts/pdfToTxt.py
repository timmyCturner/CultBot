import PyPDF2
import os
#Replace 'input.pdf' with the path to the PDF file you want to convert and 'output.txt'
#with the desired output text file path. When you run this script, it will
#extract the text content from the PDF and save it in the specified text file.

import PyPDF2

def pdf_to_text(pdf_file_path, text_file_path):
    # try:
        # Open the PDF file
        pdf_file = open(pdf_file_path, 'rb')

        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty text variable to store the extracted text
        text = ""

        # Loop through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
            
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        # Close the PDF file
        pdf_file.close()

        # Write the extracted text to a text file
        with open(text_file_path, 'w+', encoding='utf-8') as text_file:
            text_file.write(text)

        print(f"PDF successfully converted to text. Text saved in {text_file_path}")

    # except Exception as e:
    #     print(f"An error occurred: {str(e)}")

# Usage example
# pdf_file_path = 'input.pdf'  # Replace with the path to your PDF file
# text_file_path = 'output.txt'  # Replace with the desired output text file path
# import OS


for file in os.listdir("..\pdfs"):
    if file.endswith(".pdf"):
        # Prints only text file present in My Folder

        file=file[:-4]
        print(file)
        pdf_file_path = '..\\pdfs\\'+file+'.pdf'  # Replace with the path to your PDF file
        text_file_path = '..\\txts\\'+file+'.txt'  # Replace with the desired output text file path
        pdf_to_text(pdf_file_path, text_file_path)
