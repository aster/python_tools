# -*- coding: utf-8 -*-
import numpy as np
import csv
import sys

args = sys.argv

def main():
    # データのパラメータ
    dataN = 2500             #ほんとのサンプル数
    data = []
    file = args[1] #加工前データ
    window = args[2] #窓データ
    
    with open(file) as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data += [row]

    with open(window) as f:
        reader = csv.reader(f)
        win_data = []
        for row in reader:
            win_data = win_data + row

    for i in range(len(data)):
        data[i][1] = float(data[i][1]) * float(win_data[i])
        data[i][2] = float(data[i][2]) * float(win_data[i])

        print(str(data[i][1]),',',data[i][2])

if __name__ == "__main__":
    main()
