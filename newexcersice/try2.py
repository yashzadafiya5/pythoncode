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

# print(text)
textlen=len(text)
rate=int(textlen/450)
# print(textlen)
# print(rate)
lists=[]
first=0
last=300
while (last<=(textlen-300)):
    words=text[first:last]
    lists.append(words)
    first=last+1
    last=last+300
    translator=Translator(from_lang = 'en',to_lang='gu-IN')
    translation=translator.translate(words)
print(translation)
# speech = gTTS(text = str(translation), lang = 'gu', slow = False)
# speech.save("text.mp4")
# os.system("start text.mp4")
