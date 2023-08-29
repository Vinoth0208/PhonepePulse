import json
import os

import pandas as pd

top_transaction_path='pulse/data/top/transaction/country/india'
year_list=os.listdir(top_transaction_path)
topdata_all_india={'Year':[],'Quarter':[],'State_Name':[],'User_Count':[],'Amount':[]}
topdata_all_india_district={'Year':[],'Quarter':[],'District_name':[],'User_Count':[],'Amount':[]}
topdata_all_india_pincode={'Year':[],'Quarter':[],'Pincodes':[],'User_Count':[],'Amount':[]}
for i in range(len(year_list)-1):
    filepath=top_transaction_path+'/'+year_list[i]
    filelist=os.listdir(filepath)
    for j in filelist:
        file=filepath+'/'+j
        data=open(file,'r')
        all_india_transaction_data = json.load(data)
        for k in all_india_transaction_data['data']['states']:
            statename=k['entityName']
            usr_count=k['metric']['count']
            amount=k['metric']['amount']
            topdata_all_india['Year'].append(year_list[i])
            topdata_all_india['Quarter'].append(int(j.strip('.json')))
            topdata_all_india['State_Name'].append(statename)
            topdata_all_india['User_Count'].append(usr_count)
            topdata_all_india['Amount'].append(int(amount))
        for l in all_india_transaction_data['data']['pincodes']:
            pincode=l['entityName']
            count=l['metric']['count']
            amount = l['metric']['amount']
            topdata_all_india_pincode['Year'].append(year_list[i])
            topdata_all_india_pincode['Quarter'].append(int(j.strip('.json')))
            topdata_all_india_pincode['Pincodes'].append(pincode)
            topdata_all_india_pincode['User_Count'].append(count)
            topdata_all_india_pincode['Amount'].append(amount)
        for m in all_india_transaction_data['data']['districts']:
            district_name=m['entityName']
            count=m['metric']['count']
            amount = m['metric']['amount']
            topdata_all_india_district['Year'].append(year_list[i])
            topdata_all_india_district['Quarter'].append(int(j.strip('.json')))
            topdata_all_india_district['District_name'].append(district_name)
            topdata_all_india_district['User_Count'].append(count)
            topdata_all_india_district['Amount'].append(amount)
topdata_all_india_transaction_df=pd.DataFrame(topdata_all_india)
topdata_all_india_transaction_pincode_df=pd.DataFrame(topdata_all_india_pincode)
topdata_all_india_transaction_district_df=pd.DataFrame(topdata_all_india_district)

