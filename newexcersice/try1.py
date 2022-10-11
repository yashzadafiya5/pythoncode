import PyPDF2
from gtts import gTTS 
from translate import Translator
import os
pdfFileObject = open("C:/king's gym/javascript/pdf/kupdf.net_3-idiots.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

text=''
for i in range(0,pdfReader.numPages):
    # creating a page object
    pageObj = pdfReader.getPage(i)
    # extracting text from page
    text=text+pageObj.extractText()


translator=Translator(from_lang = 'en',to_lang='gu-IN')
translation=translator.translate(text)


speech = gTTS(text = str(translation), lang = 'gu', slow = False)
speech.save("text.mp3")
os.system("start text.mp3")