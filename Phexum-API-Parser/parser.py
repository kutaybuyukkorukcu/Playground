import urllib, json
import requests
with open("C://Users//90555//Desktop//Doc2.txt") as f:
  line = f.read()

line.replace(" ", "%20")
text_encoded = urllib.parse.quote(line)


api = "http://nlp.phexum.com/nlp/execute/?text=<free text>&apikey=phx595e8b79-f18c-4069-8b68-f5beebc295ac"

api = api.replace("<free text>", text_encoded)

#API Key zorunludur, kayit olduktan sonra elde edilebilir (Kayit olmak icin : http://nlp.phexum.com/)
apikey = 'phx595e8b79-f18c-4069-8b68-f5beebc295ac'

parts = {'text' : text_encoded, 'apikey' : apikey}

response = requests.get('http://nlp.phexum.com/nlp/execute/', params = parts)

data = json.loads(response.content)

for i in data["tokens"]:
  print(i["root"]) # -*- coding: utf-8 -*-

# print(data["tokens"][0]["root"])