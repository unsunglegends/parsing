import PyPDF2
from nltk.tokenize import RegexpTokenizer,sent_tokenize,word_tokenize
from nltk import pos_tag,RegexpParser
from nltk.stem import PorterStemmer
from nltk.stem import 	WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
text = "studies studying cries cry"
tokenization = word_tokenize(text)

e_words= ["wait", "waiting", "waited", "waits"]
ps =PorterStemmer()
pdfFileObj = open('IPC_186045.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(1)
test = pageObj.extractText()
tokenizer = RegexpTokenizer(r'\w+')
filterdText=tokenizer.tokenize(test)
word=word_tokenize(test)
sent=sent_tokenize(test)
#print(sent[1].split())
tokens_tag = pos_tag(sent[1].split())
print(tokens_tag,sent[1])
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = RegexpParser(grammar)
result = cp.parse(tokens_tag)
print(result)
for w in sent[1].split():
    rootWord=ps.stem(w)
    print(rootWord)
for w in word:
		print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w)))  