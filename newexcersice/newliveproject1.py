from operator import gt
import PyPDF2
from googletrans import Translator
import pyttsx3
from gtts import gTTS
import os
pdf_book=open("C:/king's gym/javascript/pdf/set2.pdf",'rb')
reading_pdf=PyPDF2.PdfFileReader(pdf_book)
pdf_speaker=pyttsx3.init()
num_pages=reading_pdf.numPages

for p in range(num_pages):
    page=reading_pdf.getPage(p)
    text=page.extract_text()


data=text.split()
text2=' '.join(data)

# ts=Translator()
output=Translator.translate(text2,dest='gu')
gujrati_text=output.text

tts=gTTS(gujrati_text,lang='gu',slow=False)
tts.save('gujju.mp3')
os.system('start gujju.mp3')