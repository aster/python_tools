import csv
import sys

args = sys.argv

for movie_index in range(1,6):
    for position_index in range(1,4):
        #print(str(movie_index) + " "+ str(position_index) )
        trimData(movie_index,position_index)
    joinTrimmedData(movie_index)
        


#データを必要な部分だけに加工する
def trimData(movie_index, position_index):

    print()
    
         
#同じ動画のフォルダ内にあるデータを結合する
def joinTrimmedData(movie_index):
    print()
    
