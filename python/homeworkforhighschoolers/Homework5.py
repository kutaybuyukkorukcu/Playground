# Kullanıcının girdiği bir metindeki her kelimenin kaçar defa tekrar ettiğini (frekansını) bulun ve bu değere göre sıralayarak gösterin.​

# Kelimelere ayırmak için, string’lerle kullanılan split yöntemini kullanabilirsiniz. Bu yöntem verilen ayıraca göre string’i böler ve her parçayı bir liste elemanı olarak belirleyip bu listeyi döndürür. Aşağıda argüman olarak sep=" " yazarak boşluklara göre böldük:​

# >>> "ali topu at".split(sep=" ")​

# ['ali', 'topu', 'at']​

""" def Sepa(x):
  words = x.split()
  unique = sorted(set(words))
  for word in unique:
    print(words.count(word), word)

def Separ(x):
  dic = {}
  word = x.split()
  for i in word:
    if not i in dic:
      dic[i] = word.count(i)
  return dic

lol = {}
lol = Separ("ali topu at karsim ali")
print(lol.items()) """

# Sayisal Loto Oynama Programi'na ekleme yapin

""" import random
ks = int(input("Kac kolon oynayacaksiniz?"))
kupon = []

for i in range(ks):
  kupon.append(set())
  while len(kupon[i]) < 6:
    kupon[i].add(random.randrange(1,50))

print("Kuponlariniz")
for i in range(ks):
  kupon[i] = list(kupon[i])
  print(sorted(kupon[i]))

def cekilis():
  setim = []
  setim.append(set())
  while len(setim[0]) < 6:
    setim[0].add(random.randrange(1,50))
  return setim[0]

liste = []
liste = list(cekilis())
kupon = list(kupon)

print("Sansli sayilar", liste)
# Cekilis yapilarak 6 sansli sayi belirlensin
# Bu sayilarin kuponumuzdaki kolonlar ile karsilastirmasi yapilir, kuponumuz tekrar print edilerek, bu defa her kolonun yaninda kac sayi 
# tutturdugumuz da yazsin
flag = 0
for n in liste:
  for i in kupon:
    for x in i:
      if (n == x):
        flag = flag + 1
  if(flag > 0):
    i.append(flag)
    print(i)
  flag = 0 """

# Gosterdigimiz sozluklerde ic ice kullanim yapisi ile birkac kayitlik bir rehber olusturun
# Bir telefon numarasi veya e-posta girdiginizde bunun kime ait old. gosterin tel(ev, is, mobil)
# Eger bulunamaz ise rehberde bulunamai, yeni kayit olarak eklemek istiyor musunuz E ise isimle rehbere ekle

rehber = {}

ad = input("ad giriniz :")
ev_tel = input("tel veya eposta giriniz :")
is_tel = input("tel veya eposta giriniz :")
mobil_tel = input("tel veya eposta giriniz :")

rehber[ad] = {"ev" : ev_tel,"is" : is_tel, "mobil" : mobil_tel}

print(rehber["Kutay"]["ev"])
