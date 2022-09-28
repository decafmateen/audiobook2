import pyttsx3
import PyPDF2


book = open('ms-17.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book, strict=False)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(8 ,pages):
    page = pdfReader.getPage(8)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
