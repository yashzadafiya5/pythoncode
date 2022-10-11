from translate import Translator
from gtts import gTTS 
import os
import PyPDF2
import pyttsx3


pdf_book=open("C:/king's gym/javascript/pdf/kupdf.net_3-idiots.pdf",'rb')
reading_pdf=PyPDF2.PdfFileReader(pdf_book)
pdf_speaker=pyttsx3.init()
num_pages=reading_pdf.numPages

for p in range(num_pages):
    page=reading_pdf.getPage(p)
    text=page.extract_text() 


data=text.split()
text2=' '.join(data)



translator=Translator(from_lang = 'en',to_lang='gu-IN')
translation=translator.translate(text2)

speech = gTTS(text = str(translation), lang = 'gu', slow = False)
speech.save("text.mp3")
os.system("start text.mp3")