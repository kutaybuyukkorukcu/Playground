import requests
from bs4 import BeautifulSoup

r = requests.get("https://yellowpages.com.tr/ara?q=cafe+&city=Istanbul")

soup = BeautifulSoup(r.content,"html.parser")
#print(soup.prettify())
#print(soup.find_all("div"))

divs = soup.find_all("div")
for div in divs:
  #print(div.get("class"))
  print(div.text)