import serial
import csv
import codecs
import sys

# 接続されてるCOMポート
com_port = 'COM3'
#保存したいファイル名
file_name = 'data.csv'

com = serial.Serial(com_port)

try:
    with open(file_name, 'w', newline='') as f:
        csvWriter = csv.writer(f)

        while True:
            line = com.readline()
            data = codecs.decode(line, 'utf-8', 'ignore')
            data = data[:-2]
            csvWriter.writerow(data.split(','))
            print(data.split(','))
except KeyboardInterrupt:
    # Ctrl-C を捕まえた！
    print('データ取得終了')
    com.close()
    sys.exit(0)