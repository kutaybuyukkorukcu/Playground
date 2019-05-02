
# Kullanıcının klavyeden girdiği sayıda Fibonacci serisi elemanını gösteren programı yazın.​

# Fibonacci serisi 0 ve 1 ile başlayıp, bir elemanın değerinin kendisinden önceki iki elemanın toplanması ile oluşturulduğu bir seridir:​

""" x = int(input("Sayi giriniz : "))

def fibo(x):
  if(x == 0):
    return 0
  elif x==1:
    return 1
  else:
    return fibo(x-1) + fibo(x-2)
#0,1,1,2,3
print(fibo(x)) """

#kanser cozum bakarsin tekrar anlamamak icin yazmislar

"""
def fibonacci(n):  
      
    # Taking 1st two fibonacci nubers as 0 and 1  
    FibArray = [0, 1]  
      
    while len(FibArray) < n + 1:  
        FibArray.append(0)  
      
    if n <= 1:  
        return n  
    else:  
        if FibArray[n - 1] == 0:  
            FibArray[n - 1] = fibonacci(n - 1)  
  
        if FibArray[n - 2] == 0:  
            FibArray[n - 2] = fibonacci(n - 2)  
              
    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]  
    return FibArray[n]  
"""

#  100 Adam ve 100 kapımız var. 1. adam 1’in katları olan kapılardan, 2. adam 2’nin katları olan kapılardan, ...., N. 
#  Adam N’in katları olan kapılardan, ... , 100. Adam 100’ün katları olan kapılardan geçerek kapıların konumlarını değiştiriyor. 
#  (Kapı açıksa kapatıyor, kapalıysa açıyor). En başta bütün kapıların kapalı olduğunu kabul edersek, 100. 
#  adam da geçtikten sonra hangi kapıların açık olduğunu bulan programı yazınız.​

""" https://www.youtube.com/watch?v=c18GjbnZXMw 
    Solve this one later on!
"""

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