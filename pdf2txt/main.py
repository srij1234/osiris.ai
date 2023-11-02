from PyPDF2 import PdfReader

reader = PdfReader("pdf2txt/test.pdf")
nop = len(reader.pages)

text=""
for i in range(nop):
    page = reader.pages[i]
    text += page.extract_text()
    

with open("pdf2txt/test.txt","w",encoding='utf-8') as f:
    f.write(text)