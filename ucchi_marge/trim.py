import csv
import sys
import glob
from pathlib import Path

args = sys.argv

def getPath(movie_index, position_index):
    file_path = './0%d/0%d/' % (movie_index, position_index)
    return file_path

# 結合するデータ一覧を取得する
def getJoinDataList(file_path):
    # csv_listに、例：動画1のベテラン20人分 のデータのPathが入ってる
    csv_list = list(glob.glob(file_path + "*.csv"))
    return csv_list

# 同じ動画番号フォルダ内にあるデータを結合する
def joinData(movie_index):
    print()

# 動画の種類（1~5）でループ  一時的に6から2に
for movie_index in range(1, 2):
    # 人の属性でループ 1:新入社員 2:1年目？ 3:ベテラン
    for position_index in range(1, 4):

        file_path = getPath(movie_index, position_index)
        join_all_list = getJoinDataList(file_path)

        for personal_data in join_all_list:
            # 個人のデータを加工して、出力用データに追加する
            # 0,1行目捨て,2行目から数字のインデックスの間を取得
            # 0列目捨て、1列目から6列分取得
            if position_index > 1:
                break
            with open(personal_data) as f:
                reader = csv.reader(f)
                first_2row = 0 

                for row in reader:
                    #最初の2行と、最後の数字以降の行を排除
                    if first_2row < 2:
                        first_2row += 1
                        continue
                    elif not row[1].isdigit() :
                        break

                    #ファイルに追記する
                    with open('filepath', 'a') as f:
                        print('aaa', file=f)
                        print(row[1:7])
