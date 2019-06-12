# -*- coding: utf-8 -*-
import numpy as np
import csv
import sys

args = sys.argv

def main():
    # 元データの数dataNと，０を付け足したデータ数Ｎ
    dataN = 2500
    N = 4096

    # サンプリング間隔(s)
    dt = 0.01

    #時間軸と周波数軸　周波数は単位を[kHz]にするため1000で割る
    t = np.arange(0, N*dt, dt)
    freq = np.linspace(0, 1.0/dt, N)/1000

    #csvデータ読み込み用配列
    data = []

    csv_file = args[1]

    with open(csv_file) as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data = data + [row]
        #print('DATA NUM ='+str(len(data)))

        # データ末尾に0を付け足す
        for i in range(N-dataN):
            data.append(['0','0'])
        #print('CHANGED DATA NUM ='+str(len(data)))

        #文字列を実数に直して，numpy配列に入れ，転置する
        f = np.array([[float(s2) for s2 in s] for s in data])
        f2 = f.T

        # 高速フーリエ変換
        Fx = np.fft.fft(f2[0])
        Fy = np.fft.fft(f2[1])
        #print(Fx.size)

        # 振幅スペクトルを計算
        Ampx = np.abs(Fx) / dataN/10 * 2
        Ampy = np.abs(Fy) / dataN/10 * 2

        for i in range(Fx.size):
            print(freq[i],',',Ampx[i],',',Ampy[i])

if __name__ == "__main__":
    main()
