import requests
from bs4 import BeautifulSoup
import operator

def create_dict(word_list):
  word_count = {}

  for word in word_list:
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1
  return word_count

def remove_symbols(word_list):
  symbol_free_words = []
  symbols = "!@#$%^&*()_+=-{}'\".,;:" + chr(775)
  for word in word_list:
    for symbol in symbols:
      if symbol in word:
        word = word.replace(symbol, "")
    
    if(len(word) > 0):
      symbol_free_words.append(word)
  return symbol_free_words

url = "http://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMgnra312w"

word_list = []

r = requests.get(url)
soup = BeautifulSoup(r.content,"lxml")

for word_groups in soup.find_all("p"):
  content = word_groups.text
  words = content.lower().split()

  for word in words:
    word_list.append(word)
    
word_list = remove_symbols(word_list)
word_count = create_dict(word_list)

for key, value in sorted(word_count.items(), key = operator.itemgetter(1),reverse=True):
  print(key, value)