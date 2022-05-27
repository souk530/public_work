import docx
import pandas as pd
import re
import csv
import glob
import os

list_file = []

target = 'ZL'
target0 = '被告'
target1 = ','
target2 = '原告'
target3 = '立案'

cols = ['案件番号','原告1','原告2','原告3','被告1','被告2','被告3','受理日','口頭弁論日','原告請求1','原告請求2','原告請求3','原告請求4','判決1','判決2','判決3','判決4','特許番号','日付']
df = pd.DataFrame(index=[],columns=cols)
df2 = pd.DataFrame(index=[],columns=cols)

for f in glob.glob('./data/docx/*.docx'):
    list_file.append(os.path.split(f)[1])

print(list_file)

def search(filename,q):
    doc = docx.Document(f'./data/docx/{filename}')
    txt = []
    #contents = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    list11 = []
    list12 = []
    list13 = []
    list14 = []
    list15 =[]
    i = 0
    j = 0
    k = 0#被告
    a = 0#原告
    w = 0#判決の指標
    target = 'ZL'
    target0 = '被告'
    target1 = ','
    target2 = '原告'
    target3 = '立案'
    target4 = '判决如下：'

    for par in doc.paragraphs:
        txt.append(par.text)

    for dot in txt:
        try:
            if ('民初' in dot and '号' in dot) and (i == 0):#最初に出てくる案件番号のみを取得
                list1.append(dot)
                i = i + 1
                df['案件番号'] = list1

                list1 = []

            elif('原告：' in dot):#原告抽出
                idt = dot.find(target2)
                dot = dot[idt+3:]
                list2.append(dot)
                if (a==0):
                    df['原告1'] = list2
                elif(a==1):
                    df['原告2'] = list2
                elif(a==3):
                    df['原告3'] = list2

                list2 = []
                a = a +1

            elif('被告：' in dot):#被告抽出
                idy = dot.find(target0)
                idz = dot.find(target1)
                dot = dot[idy+3:]
                dot = dot[:idz]
                #print(dot)
                list3.append(dot)
                #print(list3)
                if (k==0):
                    df['被告1'] = list3
                elif(k==1):
                    df['被告2'] = list3
                elif(k==3):
                    df['被告3'] = list3

                list3 = []

                k = k +1

            elif(target in dot) and (j==0):#特許番号
                j = j + 1
                #print(dot.split('\n'))
                idx = dot.find(target)
                tt = '。'
                idxx = dot.find(tt)
                dot = dot[idx:]
                dot = dot[:idxx]
                #dot = re.sub(r'\D','',dot)
                #dot = 'ZL' + dot
                dot = dot[:16]
                #print(dot)
                list4.append(dot)

                df['特許番号'] = [list4]

                list4 = []

            elif('年' in dot and '月' in dot and '日' in dot and '二'in dot):
                list5.append(dot)
                df['日付'] = list5

                list5 = []

            elif('年' in dot and '月' in dot and '日' in dot and '立案'in dot):
                ids = dot.find(target3)
                dot = dot[:ids]
                dot = re.sub(r'\D','',dot)
                list6.append(dot)
                df['受理日'] = list6

                list6 = []

            elif('于' in dot and '公开开庭进行了审理'in dot):
                dot = re.sub(r'\D','',dot)
                list15.append(dot)
                df['口頭弁論日'] = list15

                list15 = []
            #print('=======')
            elif(target4 in dot):
                key1 = 1

            elif('一、' in dot and '；' in dot and key1==1):
                list7.append(dot)
                df['判決1'] = list7

                list7 = []

            elif('二、'in dot and '；' in dot and key1==1):
                list8.append(dot)
                df['判決2'] = list8

                list8 = []

            elif('三、'in dot and '；' in dot and key1==1):
                list9.append(dot)
                df['判決3'] = list9

                list9 = []

            elif('四、'in dot and '；'in dot and key1==1):
                list10.append(dot)
                df['判決4'] = list10

                list10 = []
                key1 = 0
            elif('向本院提出诉讼请求'in dot or '请求判令' in dot and '1.' in dot):
                list11.append(dot)
                df['原告請求1'] = list11

                list11 = []
            elif('向本院提出诉讼请求'in dot or '请求判令' in dot and '2.' in dot):
                list12.append(dot)
                df['原告請求2'] = list12

                list12 = []
            elif('向本院提出诉讼请求'in dot or '请求判令' in dot and '3.' in dot):
                list13.append(dot)
                df['原告請求3'] = list13

                list13 = []
            elif('向本院提出诉讼请求' in dot or '请求判令' in dot and '4.' in dot):
                list14.append(dot)
                df['原告請求4'] = list14

                list14 = []
        except:
            continue






    df1 = pd.DataFrame(txt)
    df1.to_csv(f'textcheack{q}.csv',encoding='utf_8_sig')

    return df


r = 0

for ff in list_file:
    df = search(ff,r)
    #print('&&&&&&&&&&&&&&&&&&&&&')
    #df2.append(df)
    df.to_csv(f'{r}sample.csv',encoding='utf_8_sig')
    r = r + 1

