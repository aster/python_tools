import serial
import csv
import codecs
import sys
import os

# 接続されてるCOMポート
com_port = 'COM3'
#保存したいファイル名

# com = serial.Serial(com_port)
current_dir = os.getcwd().split('\\')[-1]
exist_files = os.listdir()
print(exist_files)
file_name = "{}".format(current_dir) +'_01'
print(file_name)

print('\n"{}"のデータを"{}"に記録します。'.format(com_port,file_name))
print('データの取得を終了するときは"Ctrl+C"\n')

sys.exit(0)

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