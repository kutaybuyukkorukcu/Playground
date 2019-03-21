# Kullanıcıdan iki sayı alan ve bu sayılar arasında yer alan tüm asal sayıları bulup bir listeye ekleyen programı yazınız.​

# Bu listenin aritmetik ortalamasını, varyansını ve standart sapmasını da hesaplayınız.​

# Varyans listedeki tüm elemanların ortalamadan farklarının eleman sayısının bir eksiğine bölümüdür.​

# Standart sapma varyansın kare köküdür.​


""" liste = []
for i in range(5,15):
  flag = 1
  for n in range(2,i//2 + 2):
    if(i % n == 0):
      flag = 0
  if(flag == 1):
    liste.append(i) """

#Varyans ve standart sapmayi siktir et

# 10 kişi için ekrandan girilen ad, soyad ve yaş bilgilerini içeren tuple tipindeki verileri bir liste içinde saklayınız.​

# Sonrasında kullanıcı ad ve soyad girerek bu liste içinde arama yapabilecek ve bulunduğu takdirde yaş değeri ekrana gösterilecek, bulunamazsa «aranan kişi bulunamadı» mesajı görüntülenecektir.​

# Arama işlemi hem ad hem de soyad için boş değer verilene kadar devam edecektir.

""" liste = []
for i in range(2):
  ad = input("ad giriniz :")
  soyad = input("soyad giriniz :")
  yas = int(input("yas giriniz :"))
  liste.append([ad, soyad, yas])

tuplem = tuple(liste)

adi, soyadi = input("yasini ogrenmek istediginiz kisinin ad ve soyadi : ").split(" ")
print([item for item in tuplem if item[0] == adi and item[1] == soyadi])
 """

#  100 Adam ve 100 kapımız var. 1. adam 1’in katları olan kapılardan, 2. adam 2’nin katları olan kapılardan, ...., N. 
#  Adam N’in katları olan kapılardan, ... , 100. Adam 100’ün katları olan kapılardan geçerek kapıların konumlarını değiştiriyor. 
#  (Kapı açıksa kapatıyor, kapalıysa açıyor). En başta bütün kapıların kapalı olduğunu kabul edersek, 100. 
#  adam da geçtikten sonra hangi kapıların açık olduğunu bulan programı yazınız.​

""" https://www.youtube.com/watch?v=c18GjbnZXMw lol """

# Romalı problemi: Roma’da Kral 21 kişinin öldürülmesine karar veriyor. Cellat fazla yorulmamak için öldürülecek olanları çember biçiminde diziyor.
# Herkesin eline bir balta veriyor. Öldürme kuralı olarak da 2. Kişi 3. Kişiyi öldürüyor. 5. Kişi 6. Kişiyi öldürüyor. 
# Yani 2 kişi atlayıp 3. kişi öldürülüyor. Bu son iki kişi kalana kadar sürüyor. Son kalan iki kişi serbest bırakılacaktır. 
# Serbest bırakılan kişilerin hangi numaralar olduğunu bulan programı yazınız.

""" Liste olusturulacak. indis 0'dan basladigi icin 1'e gore ayarlanip her seferinde 3'un kati olan indisler listeden atilacak. (pop() ile fln)
Her istenen indisi attiktan sonra zaten elimizde saf yeniden olusulmus bir liste olucak. 2 kisi kalana kadar dongu devam edip 3'un katlari atilacak
 """

# Verilen bir listeyi sort() metodunu kullanmadan sıralayan programı yazınız.​ bubble sort sıralama algoritmasını Python ile kodlamaya çalışın.

""" def bubbleSort(arr):
  n = len(arr) - 1

  for i in range(n + 1):
    for j in range(0,n-i):
      if(arr[j] > arr[j+1]):
        arr[j], arr[j+1] = arr[j+1], arr[j] """

