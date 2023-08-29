import json
import os

import pandas as pd

top_user_path='pulse/data/top/user/country/india'
year_list=os.listdir(top_user_path)
topdata_all_india={'Year':[],'Quarter':[],'State_Name':[],'RegisteredUsers':[]}
topdata_all_india_districts={'Year':[],'Quarter':[],'District_name':[],'RegisteredUsers':[]}
topdata_all_india_pincodes={'Year':[],'Quarter':[],'Pincodes':[],'RegisteredUsers':[]}
for i in range(len(year_list)-1):
    filepath=top_user_path+'/'+year_list[i]
    filelist=os.listdir(filepath)
    for j in filelist:
        file=filepath+'/'+j
        data=open(file,'r')
        all_india_user_data=json.load(data)
        for k in all_india_user_data['data']['states']:
            state_name=k['name']
            registeredUsers=k['registeredUsers']
            topdata_all_india['Year'].append(year_list[i])
            topdata_all_india['Quarter'].append(int(j.strip('.json')))
            topdata_all_india['State_Name'].append(state_name)
            topdata_all_india['RegisteredUsers'].append(registeredUsers)
        for l in all_india_user_data['data']['pincodes']:
            pincode = l['name']
            registeredUsers = l['registeredUsers']
            topdata_all_india_pincodes['Year'].append(year_list[i])
            topdata_all_india_pincodes['Quarter'].append(int(j.strip('.json')))
            topdata_all_india_pincodes['Pincodes'].append(pincode)
            topdata_all_india_pincodes['RegisteredUsers'].append(registeredUsers)
        for m in all_india_user_data['data']['districts']:
            name = m['name']
            registeredUsers = m['registeredUsers']
            topdata_all_india_districts['Year'].append(year_list[i])
            topdata_all_india_districts['Quarter'].append(int(j.strip('.json')))
            topdata_all_india_districts['District_name'].append(name)
            topdata_all_india_districts['RegisteredUsers'].append(registeredUsers)

topdata_all_india_user_df=pd.DataFrame(topdata_all_india)
topdata_all_india_user_pincodes_df=pd.DataFrame(topdata_all_india_pincodes)
topdata_all_india_user_district_df=pd.DataFrame(topdata_all_india_districts)


