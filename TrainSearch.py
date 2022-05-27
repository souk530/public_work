import json
from unittest import result
import requests
import time

url = ''
def trainsearch(worker_code, office_code):

    a_code = worker_code
    b_code = office_code
    text = str(a_code) + ':' + str(b_code)

    url_name = url + text

    list_1 = []
    l = 0
    l = l + 1

    #リクエストエラー処理
    try:
        res = requests.get(url_name)
        json_list = json.loads(res.text)
        time.sleep(0.3)
    except:
        print('request error')

    #コースが2つの場合
    try:
        #目安所要時間
        BasicOntime = int(json_list['ResultSet']['Course'][0]['Route']['timeOnBoard'])
        BasicTime_exchange = int(json_list['ResultSet']['Course'][0]['Route']['timeOther'])
        total_time = BasicOntime + BasicTime_exchange

    #コースが1つの場合
    except:
        try:
            BasicOntime = int(json_list['ResultSet']['Course']['Route']['timeOnBoard'])
            BasicTime_exchange = int(json_list['ResultSet']['Course']['Route']['timeOther'])
            total_time = BasicOntime + BasicTime_exchange
            #print("ROOT-1")

        except:
            #駅コードのミス
            total_time = '9999'
            list_1.append(url_name)

    names = []
    #駅コードが適切
    try:
        try:#コースが２つの時
            try:
                key = json_list['ResultSet']['Course'][0]['Teiki']
                names = key['DisplayRoute']

            except:
                key = json_list['ResultSet']['Course'][0]['Route']['Line']

                for i in range(len(key)):
                    name = key[i]['Name']
                    names.append(name)
        #コースが１つの時
        except:
            try:
                try:
                    key = json_list['ResultSet']['Course']['Teiki']
                    names = key['DisplayRoute']


                except:
                    key = json_list['ResultSet']['Course']['Route']['Line']

                    if json_list['ResultSet']['Course']['Route']['transferCount'] == 0:
                        names.append(json_list['ResultSet']['Course']['Route']['Line']['Name'])

                    else:
                        for i in range(len(key)):
                            name = key[i]['Name']
                            names.append(name)

            except:
                #print(key)
                name = key['Name']
                names.append(name)
    #駅コードが一致
    except:
        name = 'NULL'
        names.append(name)
        print('Same Code')



    return total_time,names,list_1
