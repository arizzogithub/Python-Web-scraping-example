import nltk
import lxml
import PyPDF2
import collections
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.probability import ConditionalFreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#from urllib2 import urlopen

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from bs4 import BeautifulSoup

# Read the URL and save text in html1 and then in text.
url1="https://www.theguardian.com/politics/2018/sep/20/the-death-of-consensus-how-conflict-came-back-to-politics"
html1 = urlopen(url1).read().decode('utf8')
BeautifulSoup(html1).get_text()
soup = BeautifulSoup(html1,'lxml')

# Read the PDF and save text in pdfString.
url2="http://eprints.lse.ac.uk/86880/7/Cox_Rise%20of%20populism%20published_2018.pdf"
pdf2 = open(url2, 'rb')
fileReader = PyPDF2.PdfFileReader(pdf2)

pdfString = ""
for x in range(11):
    pageObj = fileReader.getPage(x)
    pdfString = pdfString + pageObj.extractText()

# Print text from url2. I closed the text, but You can open it.
#print(pdfString)

text = ""
for element in soup.find_all(['title','p']):
  #print(element.text)
  text = text + element.text

# At this point, there are text and pdfString.

# Print text from url1. I closed the text, but You can open it.
#print(text)

# Collocations for url1.
words = nltk.word_tokenize(text)
string = nltk.Text(words)
print(string.collocations())

# Collocations for url2.
words = nltk.word_tokenize(pdfString)
string = nltk.Text(words)
print(string.collocations())
# Stopwords
set(stopwords.words('english'))

# Find the 24 most common words for url1.
wordcount = {}
for word in text.lower().split():

    if word not in wordcount:
      wordcount[word] = 1
    else:
      wordcount[word] += 1

word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(24):
    print(word, ": ", count)

# Stopwords
set(stopwords.words('english'))

# Find the 24 most common words for url2.
wordcount = {}
for word in pdfString.lower().split():

    if word not in wordcount:
      wordcount[word] = 1
    else:
      wordcount[word] += 1

word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(24):
    print(word, ": ", count)

