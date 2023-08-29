import json
import os

import pandas as pd

statelist=['andaman & nicobar islands', 'andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra & nagar haveli & daman & diu', 'delhi', 'goa', 'gujarat', 'haryana', 'himachal pradesh', 'jammu & kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil nadu', 'telangana', 'tripura', 'uttar pradesh', 'uttarakhand', 'west bengal']
map_user_path='pulse/data/map/user/hover/country/india'
year_list=os.listdir(map_user_path)
map_all_india={'Year': [], 'Quarter': [],'StateName':[],'RegisteredUsers':[],'AppOpens':[]}
for i in range(len(year_list)-1):
    file_path=map_user_path+'/'+year_list[i]
    file_list=os.listdir(file_path)
    for j in file_list:
        file=file_path+'/'+j
        data = open(file, 'r')
        all_india_user_data=json.load(data)
        lendata=len(all_india_user_data['data']['hoverData'])
        for k in range(lendata):
            RegisteredUsers = all_india_user_data['data']['hoverData'][statelist[k]]['registeredUsers']
            AppOpens= all_india_user_data['data']['hoverData'][statelist[k]]['appOpens']
            map_all_india['StateName'].append(statelist[k])
            map_all_india['RegisteredUsers'].append(RegisteredUsers)
            map_all_india['AppOpens'].append(AppOpens)
            map_all_india['Year'].append(year_list[i])
            map_all_india['Quarter'].append(int(j.strip('.json')))

map_all_india_usr_df=pd.DataFrame(map_all_india)
