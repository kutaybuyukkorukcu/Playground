import requests
from bs4 import BeautifulSoup

#imdb_url = "http://www.imdb.com/chart/top"

r = requests.get("http://www.imdb.com/chart/top")

soup = BeautifulSoup(r.content,"lxml")

received_data = soup.find_all("table",{"class":"chart full-width"})

movie_table = (received_data[0].contents)[len(received_data[0].contents) - 2]
movie_table = movie_table.find_all("tr")

for movie in movie_table:
  movie_titles = movie.find_all("td",{"class":"titleColumn"})
  movie_name = movie_titles[0].text
  print(movie_name)