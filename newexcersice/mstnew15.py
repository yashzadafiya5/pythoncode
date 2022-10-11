from PyPDF2 import PdfFileReader
from io import StringIO
input_path = 'newexcersice\degree certificate.pdf'

with open(input_path, 'rb') as input_file:
    input_buffer = StringIO(input_file.read())

input_pdf = PdfFileReader(input_buffer)