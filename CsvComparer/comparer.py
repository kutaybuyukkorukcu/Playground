from CSV import *
import click
import pandas as pd
import datetime
import glob

files_dir = "./files/"
def getFiles(pattern):
    return glob.glob(pattern)

input_files = getFiles(files_dir + "*.csv")

file_count = len(input_files)
data = []
table = []
file_line_number = []
files_csv = []

# Read .csv files and add significant columns
for i in range(0,file_count):
    file = input_files[i]
    data.append(file)
    csv = pd.read_csv(data[i])
    df = pd.DataFrame(csv)
    df = df[["worked_data_count","machine_used_memory","cpu_usage_rate","time"]]
    table.append(df)

# Each .csv file has it's own line
for i in range(0, file_count): 
    line_number = len(table[i])
    file_line_number.append(line_number)

# Altering tables
for i in range(0, file_count):
    maxPq = max(table[i]["worked_data_count"])
    minPq = min(table[i]["worked_data_count"])
    avgPq = (maxPq-minPq) / file_line_number[i]
    table[i].drop("worked_data_count",axis=1,inplace=False)
    table[i]["worked_data_count"] = avgPq

    table[i].drop("machine_used_memory",axis=1,inplace=False)
    table[i]["machine_used_memory"] = sum(table[i]["machine_used_memory"]) / file_line_number[i]

    memory_value = (sum(table[i]["machine_used_memory"]) / file_line_number[i] ) / (1024 * 1024 * 1024)
    table[i]["memory_as_GB"] = str(memory_value)[:7]

    cpu_value = sum(table[i]["cpu_usage_rate"]) / file_line_number[i]
    table[i].drop("cpu_usage_rate",axis=1,inplace=False)
    table[i]["cpu_usage_rate"] = cpu_value

    datetimeFormat = "%H:%M:%S"
    max_time = max(table[i]["time"])
    min_time = min(table[i]["time"])
    diff = datetime.datetime.strptime(max_time, datetimeFormat) - datetime.datetime.strptime(min_time, datetimeFormat)
    table[i].drop("time",axis=1,inplace=False)
    table[i]["time"] = diff

    file_values = table[i][:1]
    files_csv.append(file_values)

# n should be 0 and 1
def getCSVResults(files_csv, n):
    file_name = input_files[n].split("\\")[-1] 
    file_csv = files_csv[n]

    csv = CSVFile()
    csv.set_worked_data(file_csv["worked_data_count"].get(0))
    csv.set_used_memory(file_csv["machine_used_memory"].get(0))
    csv.set_total_memory(file_csv["memory_as_GB"].get(0))
    csv.set_cpu_usage(file_csv["cpu_usage_rate"].get(0))
    csv.set_time(file_csv["time"].get(0).total_seconds())
    return csv


@click.command()
@click.option('--compare', help = 'Will compare specific .csv files')
def cli():


    click.echo('''
        |||||||||||
        ||| work_time    
    

    
    
    
    ''')

