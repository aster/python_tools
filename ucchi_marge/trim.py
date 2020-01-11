import csv
import sys
from pathlib import Path

args = sys.argv

#結合するデータ一覧を取得する
def trimData(movie_index, position_index):
    file_path = './0%d/0%d/' % (movie_index, position_index)
    print(file_path)
    csv_list = list(file_path.glob("*.csv"))

#データを結合する

         

#同じ動画番号フォルダ内にあるデータを結合する
def joinTrimmedData(movie_index):
    print()
    

for movie_index in range(1,6):
    for position_index in range(1,4):
        #print(str(movie_index) + " "+ str(position_index) )
        trimData(movie_index,position_index)
    #joinTrimmedData(movie_index)
        

