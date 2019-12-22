import PyPDF2
import re
from nltk.tokenize import RegexpTokenizer,sent_tokenize,word_tokenize

# pdf file object
# you can find find the pdf file with complete code in below
pdfFileObj = open('IPC_186045.pdf', 'rb')
# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# a page object
pageObj = pdfReader.getPage(52)
# extracting text from page.
# this will print the text you can also save that into String
test = pageObj.extractText()

tokenizer = RegexpTokenizer(r'\w+')
filterdText=tokenizer.tokenize(test)
word=word_tokenize(test)
sent=sent_tokenize(test)

print(sent[0].split())