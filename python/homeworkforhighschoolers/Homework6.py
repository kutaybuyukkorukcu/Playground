""" def per(eleman_sayisi, secilen_eleman_sayisi):
  return fac(eleman_sayisi) / fac(eleman_sayisi - secilen_eleman_sayisi)

def kom(eleman_sayisi, secilen_eleman_sayisi):
  return fac(eleman_sayisi)/ fac(eleman_sayisi - secilen_eleman_sayisi) * fac(secilen_eleman_sayisi)

def fac(sayi):
  if(sayi == 1):
    return 1
  return fac(sayi-1) * sayi
 """
#Asagidakiler modulun import edildigi dosya da yazilacak
""" 
eleman_sayisi = int(input("eleman sayisi giriniz :"))
secilen_eleman_sayisi = int(input("secmek istediginiz eleman sayisi giriniz :"))

if(!(eleman_sayisi < 0 or secilen_eleman_sayisi < 0) and eleman_sayisi - secilen_eleman_sayisi > 0):
  print("duzgun inputlar giriniz")
 """

#Sayiyi yazi olarak bastiran fonksiyon yaziniz
#694 -> altiyuzdoksandort 1253 -> binikiyuzelliuc

def print_as_string(sayi):
  "Son iki rakam okunur, onceki basamaklar yuz, bin olarak yazilir"
  listem = [int(x) for x in str(sayi)]
  bas_sayisi = len(listem)
  ones = ["","bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz"]
  tens = ["","on","yirmi","otuz","kirk","elli","altmis","yetmis","seksen","doksan"]
  hundreds = ["","yuz","ikiyuz","ucyuz","dortyuz","besyuz","altiyuz","yediyuz","sekizyuz","dokuzyuz"]
  thousands = ["","bin","ikibin","ucbin","dortbin","besbin","altibin","yedibin","sekizbin","dokuzbin"]
  if(bas_sayisi == 1):
    print(ones[int(listem[0])])
  elif(bas_sayisi == 2):
    print(tens[int(listem[1])] + ones[int(listem[0])])
  elif(bas_sayisi == 3):
    print(hundreds[int(listem[2])] + tens[int(listem[1])] + ones[int(listem[0])])
  elif(bas_sayisi == 4):
    print(thousands[int(listem[3])] + hundreds[int(listem[2])] + tens[int(listem[1])] + ones[int(listem[0])])
  else:
    print("OMEGALUL")

def dost(sayi1, sayi2):
  if(bolen_toplami(sayi1) == sayi2):
    print("Girilen iki sayida dost sayidir")

def bolen_toplami(sayi):  
  sum = 0
  for i in range(1,sayi):
    if(sayi % i == 0):
      sum = sum + i 
  return sum

dost(220, 284)