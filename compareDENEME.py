import webbrowser
import pandas as pd
import datetime
import glob

files_dir="./files/"
def getFiles(pattern):
    return glob.glob(pattern)

def getScripts(): # prints //jquery.js
    all_scripts = ""
    scripts=getFiles("./js/*.js")
    for sf in scripts:
        f = open(sf,"r")
        all_scripts +=  "\r\n//"+sf+"\r\n" + f.read()
        f.close()
    return all_scripts

input_files=getFiles(files_dir + "*.csv")

csvCount = len(input_files)
data = []
table = []
rowSayisi = []
csvFile = []
#usecols ile istenen sutunlari okutabiliriz
for i in range(0,csvCount): #csv dosyalarinin pathlerini data listesine yaz
    plsWork = input_files[i]
    data.append(plsWork)

for i in range(0,csvCount): #data pathlerini oku ve table listesine yaz
    plsWork2 = pd.read_csv(data[i])
    df = pd.DataFrame(plsWork2)
    df = df[["worked_data_count","machine_used_memory","cpu_usage_rate","time"]]
    table.append(df)

#csv_sutun_isimleri = ["worked_data_count","machine_used_memory","cpu_usage_rate","time"]
#for i in range(0,csvCount): #Her table icin sutun ata
#    table[i].columns = csv_sutun_isimleri

for i in range(0,csvCount):  #Her table icin farkli bir row sayisi olmali
    plsWork3 = len(table[i])
    rowSayisi.append(plsWork3)

for i in range(0,csvCount): #alter table islemi
    maxPq = max(table[i]["worked_data_count"])
    minPq = min(table[i]["worked_data_count"])
    avgPq = (maxPq-minPq) / rowSayisi[i]
    table[i].drop("worked_data_count",axis=1,inplace=False)
    table[i]["worked_data_count"] = avgPq

    memoryV = sum(table[i]["machine_used_memory"]) / rowSayisi[i]
    table[i].drop("machine_used_memory",axis=1,inplace=False)
    table[i]["machine_used_memory"] = memoryV

    memoryV = (sum(table[i]["machine_used_memory"]) / rowSayisi[i] ) / (1024 * 1024 * 1024)
    table[i]["memory_as_GB"] = str(memoryV)[:7]

    #memoryV / (1024 * 1024 * 1024)
    #print(memoryV)

    cpuV = sum(table[i]["cpu_usage_rate"]) / rowSayisi[i]
    table[i].drop("cpu_usage_rate",axis=1,inplace=False)
    table[i]["cpu_usage_rate"] = cpuV

    datetimeFormat = "%H:%M:%S"
    maxT = max(table[i]["time"])
    minT = min(table[i]["time"])
    diff = datetime.datetime.strptime(maxT, datetimeFormat) - datetime.datetime.strptime(minT, datetimeFormat)
    table[i].drop("time",axis=1,inplace=False)
    table[i]["time"] = diff

    plsWork4 = table[i][:1]
    csvFile.append(plsWork4)

json = {}
jsonResultObject={}

for n in range(0,len(csvFile)):
    file_name = input_files[n]
    file_name = file_name.split("\\")[-1] # windows icin belki?! \\
    e = csvFile[n]
    json["worked_data_count"]=e["worked_data_count"].get(0)
    json["machine_used_memory"]=e["machine_used_memory"].get(0)
    json["memory_as_GB"] = e["memory_as_GB"].get(0)
    json["cpu_usage_rate"]=e["cpu_usage_rate"].get(0)
    json["time"]=e["time"].get(0).total_seconds()
    #print (json)
    jsonResultObject[file_name]=json
    print (jsonResultObject)

file=open("./compare.html","r")
compare = file.read()
file.close()
compare = compare.replace("{{output}}" , str(jsonResultObject))
compare = compare.replace("{{scripts}}" , getScripts())
outfile = open("compare.html","w")
outfile.write(compare)
outfile.close()