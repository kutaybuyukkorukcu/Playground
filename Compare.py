import pandas as pd
import datetime
"""
#self refers to the object
class dataStruct:
    def rowCount(self,x):
        row_count = sum(1 for row in x) + 1
        return(row_count)
    def timeDiff(self,x):
        datetimeFormat = "%H:%M"
        maxT = max(x["TIME"])
        minT = min(x["TIME"])
        diff = datetime.datetime.strptime(maxT, datetimeFormat) - datetime.datetime.strptime(minT, datetimeFormat)
        return diff
    def returnPQ(self,x):
        pqV = sum(x["PQ"])
        return pqV
    def returnCPU(self,x):
        cpuV = sum(x["CPU"]) / dataStruct.row_count(x)
        return cpuV
    def returnMEMORY(self,x):
        memoryV = sum(x["MEMORY"]) / dataStruct.row_count(x)
        return memoryV
    def printCPU(self,x):
        print(dataStruct.returnCPU(x))

data1 = input("Select the first csv file you want to compare :")
table1 = pd.read_csv(data1)
csv_columnname = ["TIME", "PQ", "CPU", "MEMORY"]
table1.columns = csv_columnname
first = dataStruct()
anan = first.returnCPU(table1)
print(first.printCPU(anan))
#self equals first in this case

"""
"""
data1 = input("Select the first csv file you want to compare :")
table1 = pd.read_csv(data1)
csv_columnname = ["TIME", "PQ", "CPU", "MEMORY"]
table1.columns = csv_columnname
"""

"""
csvCount = int(input("Kac tane csv dosyasi karsilastiracaksiniz?"))
data = []
table = []
rowSayisi = []
csvFile = []
#usecols ile istenen sutunlari okutabiliriz
for i in range(0,csvCount): #csv dosyalarinin pathlerini data listesine yaz
    plsWork = input("i. csv dosyasinin pathini giriniz : ")
    data.append(plsWork)

for i in range(0,csvCount): #data pathlerini oku ve table listesine yaz
    plsWork2 = pd.read_csv(data[i])
    table.append(plsWork2)
#ozel kolon secme yerine kullanicidan kolon isimlerini duzgun sekilde girilmis bir csv dosyasi bekleyip belirli sutunlari mi secelim
csv_sutun_isimleri = ["TIME","PQ","CPU","MEMORY"]
for i in range(0,csvCount): #Her table icin sutun ata
    table[i].columns = csv_sutun_isimleri

for i in range(0,csvCount):  #Her table icin farkli bir row sayisi olmali
    plsWork3 = sum(1 for row in table[i]) + 1
    rowSayisi.append(plsWork3)

for i in range(0,csvCount): #alter table islemi
    datetimeFormat = "%H:%M"
    maxT = max(table[i]["TIME"])
    minT = min(table[i]["TIME"])
    diff = datetime.datetime.strptime(maxT, datetimeFormat) - datetime.datetime.strptime(minT, datetimeFormat)
    table[i].drop("TIME",axis=1,inplace=False)
    table[i]["TIME"] = diff
    pqV = sum(table[i]["PQ"])
    table[i].drop("PQ",axis=1,inplace=False)
    table[i]["PQ"] = pqV
    cpuV = sum(table[i]["CPU"]) / rowSayisi[i]
    table[i].drop("CPU",axis=1,inplace=False)
    table[i]["CPU"] = cpuV
    memoryV = sum(table[i]["MEMORY"]) / rowSayisi[i]
    table[i].drop("MEMORY",axis=1,inplace=False)
    table[i]["MEMORY"] = memoryV
    plsWork4 = table[i][:1]
    csvFile.append(plsWork4)
    print(csvFile[i])
"""


"""
datetimeFormat = "%H:%M"
maxT = max(table[i]["TIME"])
minT = min(table[i]["TIME"])
diff = datetime.datetime.strptime(maxT, datetimeFormat) - datetime.datetime.strptime(minT, datetimeFormat)
pqV = sum(table[i]["PQ"])
calculated.append(pqV)
cpuV = sum(table[i]["CPU"]) / row_count
calculated.append(cpuV)
memoryV = sum(table[i]["MEMORY"]) / row_count
calculated.append(memoryV)
print(calculated[0])

"""

"""

def properties():
    datetimeFormat = "%H:%M"
    maxT = max(table[i]["TIME"])
    minT = min(table[i]["TIME"])
    diff = datetime.datetime.strptime(maxT, datetimeFormat) - datetime.datetime.strptime(minT, datetimeFormat)
    pqV = sum(table[i]["PQ"])
    cpuV = sum(table[i]["CPU"]) / row_count    
    memoryV = sum(table[i]["MEMORY"]) / row_count

"""








"""
data1 = input("Select the first csv file you want to compare :")
data2 = input("Select the second csv file you want to compare :")
table1 = pd.read_csv(data1)
table2 = pd.read_csv(data2)
csv_columnname = ["TIME", "PQ", "CPU", "MEMORY"]
table1.columns = csv_columnname
table2.columns = csv_columnname
printProp(table1)
printProp(table2)
"""

"""
data = [line.strip() for line in open("C:/users/kutay/desktop/request.csv", 'r')]
print(data)
with open('C:/users/kutay/desktop/request.csv') as f:
    lines = f.read().splitlines()
print(lines) 

with open('C:/users/kutay/desktop/request.csv','r') as file:
    for line in file:
        print(line[0:line.find(',')])

data2 = [line.strip() for line in open("C:/users/kutay/desktop/request1.csv",'r')]
row_sayisi = len(data) - 1
column_sayisi = 4 # koda dokemedim 4 kolon olmak zorunda sarti koydum
#print(data)
#for i in range(0,column_sayisi):
    #for n in range(0,row_sayisi):
#matrix = [data[i:i+1] for i in range(0,len(data))]
#trinity = [data[i:i+1] for i in range(0,len(data2))]
#for i in matrix:
#    print(i)
#print(data[3][3])
#for i in trinity:
   # print(i)
"""


"""
csvCount = int(input("kac csv dosyasi okutacaksin"))
for i in range(1,csvCount+1):
    print()
"""