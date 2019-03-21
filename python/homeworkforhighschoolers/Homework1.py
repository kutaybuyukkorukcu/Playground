# Saniye olarak verilen değeri saat:dakika:saniye olarak gösteren programı yazın.​

# süreyi girin (sn): 100​

# 0:1:40​

# süreyi girin (sn): 1000​

# 0:16:40​

# süreyi girin (sn): 8000​ -> input
# 2:13:20​ -> print

x = int(input("Saniye giriniz : "))

a = x / 3600 
x = x % 3600
b = x / 60
x = x % 60
c = x

print("Saat: %d, Dakika: %d, Saniye: %d" % (a,b,c))

#############################################################

# Başlangıç koordinatı, fırlatma hızı ve geçen süre verildiğinde bir nesnenin son koordinatını hesaplayan programı yazın (g=9.81).​

# Başlangıç x koordinatı: -1.4​

# Başlangıç y koordinatı: 4.5​

# Fırlatma x hızı: 2.34​

# Fırlatma y hızı: 12.4​

# Geçen süre (sn): 5.6​

# Sonuç x koodinatı: 11.704​

# Sonuç y koodinatı: -79.8808​
"""
x = int(input("x koordinatini giriniz : "))
y = int(input("y koordinatini giriniz : "))
vX = int(input("x hizi : "))
vY = int(input("y hizi : "))
t = int(input("t'yi giriniz : "))
"""
##############################################################
