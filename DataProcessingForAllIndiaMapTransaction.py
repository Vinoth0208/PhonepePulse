import json
import os

import pandas as pd

map_transaction_path='pulse/data/map/transaction/hover/country/india'
year_list=os.listdir(map_transaction_path)
map_all_india={'Year': [], 'Quarter': [],'Name':[],'User_count':[],'Amount':[]}
for i in range(len(year_list)-1):
    file_path=map_transaction_path+'/'+year_list[i]
    file_list=os.listdir(file_path)
    for j in file_list:
        file=file_path+'/'+j
        data = open(file, 'r')
        all_india_transaction_data=json.load(data)
        all_india_map_transaction_data=all_india_transaction_data['data']['hoverDataList']
        for k in all_india_map_transaction_data:
            Name=k['name']
            User_Count=k['metric'][0]['count']
            Amount = k['metric'][0]['amount']
            map_all_india['Year'].append(year_list[i])
            map_all_india['Quarter'].append(int(j.strip('.json')))
            map_all_india['Name'].append(Name)
            map_all_india['Amount'].append(int(Amount))
            map_all_india['User_count'].append(User_Count)

map_all_india_transaction_df=pd.DataFrame(map_all_india)


