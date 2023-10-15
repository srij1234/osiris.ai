from PyPDF2 import PdfReader

reader = PdfReader("test.pdf")
nop = len(reader.pages)

text=""
for i in range(nop):
    page = reader.pages[i]
    text += page.extract_text()
    

with open("text.txt","w",encoding='utf-8') as f:
    f.write(text)