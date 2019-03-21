#for dongusu ile 2 tane ucgen ciz

""" satir = int(input("Kac satirli olsun : "))
yildiz_sayisi_per_satir = satir * 2
for i in range(1,satir + 1):
  #print(satir * " " + i * 2 * "*") Duz 
  print(i * " " + satir * 2 * "*") #Ters
  satir -= 1
 """

# Sayının yarısına kadar değil, daha da az sayıda döngü adımı ile asal sayı bulabilen bir yöntem bularak kodunu yazın.​

""" sayi = int(input("Sayi giriniz : "))
for i in range(2, sayi//2):
  if(sayi % i == 0):
    print("Sayi asal degil")
    break
print("Sayi asal")
 """

# 1 ile 1000 arasındaki mükemmel sayıları bulan ve ekranda görüntüleyen programı yazın.​

# Bölenlerinin toplamı kendisine eşit olan sayılar mükemmel sayıdır. Örn: 28 = 1+2+4+7+14.​

for i in range(1,1000):
  sum = 0
  for n in range(1,i):
    if(i % n == 0):
      sum = sum + n 
  if(sum == i):
    print(i, "mukemmel")


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