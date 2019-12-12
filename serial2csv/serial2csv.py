import serial
import csv
import codecs
import sys
import os

# 接続されてるCOMポート
com_port = 'COM3'

com = serial.Serial(com_port)

current_dir = os.getcwd().split('\\')[-1]
file_name = "{}".format(current_dir)

print("今いるディレクトリは"+file_name+"です")
file_num = input('データの番号を入力してください -> ').zfill(2)

print('\n"{}"のデータを"{}"に記録します。'.format(com_port,file_name+'_'+file_num+'.csv'))
print('データの取得を終了するときは"Ctrl+C"\n')

file_name = file_name+'_'+file_num+'.csv'

try:
    with open(file_name, 'w', newline='') as f:
        csvWriter = csv.writer(f)

        while True:
            line = com.readline()
            data = codecs.decode(line, 'utf-8', 'ignore')
            data = data[:-2]

            #ここでdataを加工
            #data -> 10005,3
            a = 1
            b = 1
            data = data + "," + str(a) + "," + str(b)
            #ここまで

            csvWriter.writerow(data.split(','))
            print(data.split(','))
except KeyboardInterrupt:
    # Ctrl-C を捕まえた！
    print('データ取得終了')
    com.close()
    sys.exit(0)