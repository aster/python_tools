import serial
import csv
import codecs

# 接続されてるCOMポート
com_port = 'COM3'
#保存したいファイル名
file_name = 'data.csv'

com = serial.Serial(com_port)
f = open(file_name, 'w', newline='')
csvWriter = csv.writer(f)

# while 0: 
while True:
    listData = []
    line = com.readline()
    data = codecs.decode(line, 'utf-8', 'ignore')
    data = data[:-2]
    print(data.split(','))
    csvWriter.writerow(data.split(','))

com.close()
