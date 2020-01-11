import csv
import sys
import glob
from pathlib import Path

args = sys.argv

#結合するデータ一覧を取得する
def trimData(movie_index, position_index):
    file_path = './0%d/0%d/' % (movie_index, position_index)

    #csv_listに、例：動画1のベテラン20人分 のデータのPathが入ってる
    csv_list = list(glob.glob(file_path + "*.csv"))
    return csv_list

#データを結合する
         

#同じ動画番号フォルダ内にあるデータを結合する
def joinTrimmedData(movie_index):
    print()
    
#動画の種類（1~5）でループ
for movie_index in range(1,6):
    #人の属性でループ 1:新入社員 2:1年目？ 3:ベテラン
    for position_index in range(1,4):
        #print(str(movie_index) + " "+ str(position_index) )
        trimData(movie_index,position_index)
    #joinTrimmedData(movie_index)
        

