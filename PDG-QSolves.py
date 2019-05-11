
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

# Yükseklik ve genişlik niteliklerine sahip olan, bunları kullanarak alan ve çevre hesaplaması için ilgili yöntemleri de içeren bir Dikdörtgen sınıfı yazınız.​

# Kenar niteliğine sahip olan ve Dikdörtgen sınıfındaki yöntemleri miras alıp çevre ve alan hesaplayan Kare sınıfını yazınız.​

# Yükseklik ve taban niteliklerine ve kendi çevre yöntemine sahip olan alan yöntemini ise Dikdörtgen sınıfından miras alan ParalelKenar sınıfını yazınız.​

# İkizKenarÜçgen sınıfı ise yükseklik ve taban niteliklerini ParalelKenar sınıfından miras alacak ama çevre ve alan hesabı için kendi yöntemlerini kullanması gerekecektir.​

# Kare hariç her sınıfta verilen bir sembol ile ilgili genişlik, yükseklik, taban, kenar değerlerine göre şekli çizdiren bir çizdir yöntemi yazınız. Kare ise Dikdörtgen’den miras aldığı yöntemi kullanabilecektir. ​

# 3. hafta yaptığımız üçgen çizimlerinde sembol olarak hep '*' kullanılmıştı, mantık benzer olacak ama sembol değiştirilebilecek​

# Ali,SOLMAZ,60​

# Selman,ÇIKMAZ,90​

# Bahri,SEZGİN,80​

# Selçuk,KIRGIZ,45​

# Kemal,GÜNEŞ,55​

# Ahmet,ÇALIŞKAN,75

# ukarıdaki gibi içeriğe sahip bir "sınavsonuçları.txt" dosyasına sahip olduğunuzu düşünün.​

# Sınava giren tüm öğrencilerin adı, soyadı ve sınav sonucu saklanmış olan bu dosyada her kayıt ayrı bir satıra yazılmış ve değerler arasında virgül kullanılmıştır.​

# Bu tip dosyalar CSV (comma seperated values) olarak bilinir.​

# Yazacağınız program bu dosyayı okuyup sınav sonucu 60 ve üzerinde olan öğrencileri ve notlarını aynı biçimde yeni yaratacağı "geçenler.txt" dosyasına, diğerlerini de yeni yarayacağı "kalanlar.txt" dosyasına yazsın.​

# Kullanıcının ekleyeceği notları notlar.txt dosyasında sıra ile saklayan bir program yazın. Program çalıştırıldığında dosyanın içinde saklı olan tüm notlar sıra numarası ile birlikte görüntülenecek ve altında "not eklemek için 1’e, not silmek için 2’ye çıkış için ESC’ye basın" mesajı görüntülenecektir.​

# Not Ekleme seçildiğinde "Notunuzu Giriniz" mesajı görüntülenecek ve kullanıcının ekrana yazacağı not ENTER basıldığı anda dosyanın sonuna eklenecektir.​

# Not Silme seçildiğinde "Silmek İstediğiniz Notun Numarasını Giriniz" mesajı görüntülenecek ve kullanıcının seçtiği not dosyadan silinecektir.​

# Ekleme ve silme işlemlerinden sonra ekran temizlenip programın başına dönülmelidir (Dosyanın son hali ekranda gösterilip yine altında "not eklemek için 1’e, not silmek için 2’ye çıkış için ESC’ye basın" mesajı görüntülenmelidir).​

# SQLite üzerinde saklanacak bir telefon rehberi oluşturun.​

# Rehberiniz aynı kişiye ait birçok telefon numarası saklanabilecek bir yapıda olsun.​

# Programınızda bir menü olsun ve ilgili seçenekler seçildiğinde kayıtlar üzerinde arama, ekleme, silme ve güncelleme (tel numarasını değiştirme gibi) işlemleri yapılabilsin.​

# Arama yaparken iki seçenek olsun: Hem telefon numarası verilip ilgili isim getirilebilsin, hem de isim verilip telefon numarası getirilebilsin.