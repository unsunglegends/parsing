from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer,sent_tokenize,word_tokenize
stopwords = stopwords.words("english")
stopwords.append('Act')
text = 'Act likely to cause harm, but done without criminal intent, and to prevent other harm.'
words =  word_tokenize(text)
filtered = [w for w in words if not w in stopwords ]
print(filtered)