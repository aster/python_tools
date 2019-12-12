import serial
import csv

# 接続されてるCOMポート
com_port = 'COM3'
#保存したいファイル名
file_name = 'data.csv'

com = serial.Serial(com_port)
f = open(file_name, 'wb')
csvWriter = csv.writer(f)

while True:
    listData = []
    line = com.readline()
    data = line.split(",")
    del data[-1]
    print data
    csvWriter.writerow(data)

com.close()
