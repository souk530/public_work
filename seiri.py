import csv
import glob
import os
import pandas as pd


list_file = []
contents = []


for f in glob.glob('*sample.csv'):
    list_file.append(os.path.split(f)[1])
print(list_file)


for file_name in list_file:
    with open(f'{file_name}','r',encoding='utf_8_sig') as l:
        reader = csv.reader(l)
        next(reader)
        for row in reader:
            contents.append(row)
            #print(row)

#print(contents)
#cols = ['top','案件番号','原告1','原告2','原告3','被告1','被告2','被告3','受理日','口頭弁論日','原告請求1','原告請求2','原告請求3','原告請求4','判決1','判決2','判決3','判決4','特許番号','日付']

df = pd.DataFrame(contents)
df.to_csv('resres.csv',encoding='utf_8_sig')

