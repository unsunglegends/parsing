import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import PyPDF2

def readpdf():
    pdfFileObj = open('IPC_186045.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    return pdfReader

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


out = readpdf()
pageObj=out.getPage(1)
train_test = pageObj.extractText()
spageObj=out.getPage(2)
sample_test = spageObj.extractText() 
print(sample_test)
#custom_sent_tokenizer = PunktSentenceTokenizer(train_test)
#tokenized = custom_sent_tokenizer.tokenize(sample_test)
#process_content()
