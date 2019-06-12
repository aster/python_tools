###########################################
# usage                                   #
# >> python3  change.py  (filename).csv   #
###########################################
import sys
import csv
import math
args = sys.argv

# サンプリング周期(s)
dt = 0.01
# 初期時間
t = 0.0
# データの最初からX点までの平均を基準とする
X = 300

tmpCnt = 0
tmpTotal = [0.0, 0.0]

with open(args[1], "r", newline="") as csv_file:
    f = csv.reader(csv_file)

    # 基準値の計算
    for row in f:
        tmpTotal[0] += float(row[4])
        tmpTotal[1] += float(row[10])
        tmpCnt += 1
        if tmpCnt > X:
            break

    offsetX = tmpTotal[0]/X
    offsetY = tmpTotal[1]/X

    # 途中まで進んだイテレータを戻す
    csv_file.seek(0)

    # 出力用データの処理
    for row in f:
        print(round(t, 4), ',', math.degrees(math.asin((float(row[4]) - offsetX) / 4.0)),
                ',', math.degrees(math.asin((float(row[10]) - offsetY) / 4.0)))

        t += dt
