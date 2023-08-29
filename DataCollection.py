import json
import os

import pandas as pd

os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git
if not os.path.exists(r'C:\Users\Vinoth\PycharmProjects\PhonepePulse\pulse'):
    os.system("git clone https://github.com/PhonePe/pulse.git")
ag_tr_st_path = r"C:\Users\Vinoth\PycharmProjects\PhonepePulse\pulse\data\aggregated\transaction\country\india\state"
ag_tr_st_list=os.listdir(ag_tr_st_path)

ag_tr = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [], 'Transaction_amount': []}
for i in ag_tr_st_list:
    ag_tr_st_yr_path=ag_tr_st_path+'/'+i
    ag_tr_st_yr_list=os.listdir(ag_tr_st_yr_path)
    for j in ag_tr_st_yr_list:
        ag_tr_st_yr_file_path=ag_tr_st_yr_path+'/'+j
        ag_tr_st_yr_file_list=os.listdir(ag_tr_st_yr_file_path)
        for k in ag_tr_st_yr_file_list:
            file=ag_tr_st_yr_file_path+'/'+k
            data=open(file,'r')
            tr_data=json.load(data)

            for l in tr_data['data']['transactionData']:
                Name=l['name']
                count = l['paymentInstruments'][0]['count']
                amount = l['paymentInstruments'][0]['amount']
                ag_tr['State'].append(i)
                ag_tr['Year'].append(j)
                ag_tr['Quarter'].append(int(k.strip('.json')))
                ag_tr['Transaction_type'].append(Name)
                ag_tr['Transaction_count'].append(count)
                ag_tr['Transaction_amount'].append(amount)
ag_tr_df=pd.DataFrame(ag_tr)

ag_usr_path=r'C:\Users\Vinoth\PycharmProjects\PhonepePulse\pulse\data\aggregated\user\country\india\state'
ag_usr_st_list=os.listdir(ag_usr_path)
ag_usr = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'UsrCount': [], 'Percentage': []}
for i in ag_usr_st_list:
    ag_usr_st_yr_path=ag_usr_path+'/'+i
    ag_usr_st_yr_list=os.listdir(ag_usr_st_yr_path)
    for j in ag_usr_st_yr_list:
        ag_usr_st_yr_file_path=ag_usr_st_yr_path+'/'+j
        ag_usr_st_yr_file_list=os.listdir(ag_usr_st_yr_file_path)
        for k in ag_usr_st_yr_file_list:
            file=ag_usr_st_yr_file_path+'/'+k
            data= open(file,'r')
            usr_data=json.load(data)
            try:
                for l in usr_data['data']['usersByDevice']:
                    brand=l['brand']
                    count=l['count']
                    percentage=l['percentage']
                    ag_usr['State'].append(i)
                    ag_usr['Year'].append(j)
                    ag_usr['Quarter'].append(int(k.strip('.json')))
                    ag_usr['Brands'].append(brand)
                    ag_usr['UsrCount'].append(count)
                    ag_usr['Percentage'].append(percentage*100)
            except:
                pass
usr_ag_df=pd.DataFrame(ag_usr)


map_tr_st_path=r'C:\Users\Vinoth\PycharmProjects\PhonepePulse\pulse\data\map\transaction\hover\country\india\state'
map_tr_st_list=os.listdir(map_tr_st_path)
map_tr = {'State': [], 'Year': [], 'Quarter': [], 'District_name': [], 'Transaction_count': [], 'Transaction_amount': []}
for i in map_tr_st_list:
    map_tr_st_yr_path=map_tr_st_path+'/'+i
    map_tr_st_yr_list=os.listdir(map_tr_st_yr_path)
    for j in map_tr_st_yr_list:
        map_tr_st_yr_file_path=map_tr_st_yr_path+'/'+j
        map_tr_st_yr_file_list=os.listdir(map_tr_st_yr_file_path)
        for k in map_tr_st_yr_file_list:
            file = map_tr_st_yr_file_path + '/' + k
            data = open(file, 'r')
            map_tr_data = json.load(data)
            for l in map_tr_data['data']['hoverDataList']:
                district_name=l['name']
                tr_count=l['metric'][0]['count']
                tr_amount=tr_count=l['metric'][0]['amount']
                map_tr['State'].append(i)
                map_tr['Year'].append(j)
                map_tr['Quarter'].append(int(k.strip('.json')))
                map_tr['District_name'].append(district_name)
                map_tr['Transaction_count'].append(count)
                map_tr['Transaction_amount'].append(tr_amount)
tr_map_df=pd.DataFrame(map_tr)


map_usr_st_path=r'C:\Users\Vinoth\PycharmProjects\PhonepePulse\pulse\data\map\user\hover\country\india\state'
map_usr_st_list=os.listdir(map_usr_st_path)
map_usr = {'State': [], 'Year': [], 'Quarter': [], 'District_name': [], 'RegisteredUsers': [], 'AppOpens': []}
for i in map_usr_st_list:
    map_usr_st_yr_path=map_usr_st_path+'/'+i
    map_usr_st_yr_list=os.listdir(map_usr_st_yr_path)
    for j in map_usr_st_yr_list:
        map_usr_st_yr_file_path=map_usr_st_yr_path+'/'+j
        map_usr_st_yr_file_list=os.listdir(map_usr_st_yr_file_path)
        for k in map_usr_st_yr_file_list:
            file = map_usr_st_yr_file_path + '/' + k
            data = open(file, 'r')
            map_usr_data = json.load(data)
            for l in map_usr_data['data']['hoverData']:
                dt_name=l
                registeredUsers=map_usr_data['data']['hoverData'][l]['registeredUsers']
                appOpens=map_usr_data['data']['hoverData'][l]['appOpens']
                map_usr['State'].append(i)
                map_usr['Year'].append(j)
                map_usr['Quarter'].append(int(k.strip('.json')))
                map_usr['District_name'].append(dt_name)
                map_usr['RegisteredUsers'].append(registeredUsers)
                map_usr['AppOpens'].append(appOpens)
usr_map_df=pd.DataFrame(map_usr)

tp_tr_st_path=r'C:\Users\Vinoth\PycharmProjects\PhonepePulse\pulse\data\top\transaction\country\india\state'
tp_tr_st_list=os.listdir(tp_tr_st_path)
tp_tr={'State': [], 'Year': [], 'Quarter': [],'District_name':[], 'Count':[], 'Amount':[]}
tp_trp={'State': [], 'Year': [], 'Quarter': [],'Pincodes':[],'Pincode_count':[],'Pincode_amount':[]}
for i in tp_tr_st_list:
    tp_tr_st_yr_path=tp_tr_st_path+'/'+i
    tp_tr_st_yr_list=os.listdir(tp_tr_st_yr_path)
    for j in tp_tr_st_yr_list:
        tp_tr_st_yr_file_path=tp_tr_st_yr_path+'/'+j
        tp_tr_st_yr_file_list=os.listdir(tp_tr_st_yr_file_path)
        for k in tp_tr_st_yr_file_list:
            file = tp_tr_st_yr_file_path + '/' + k
            data = open(file, 'r')
            top_tr_data = json.load(data)
            for l in top_tr_data['data']['districts']:
                dt_name=l['entityName']
                count=l['metric']['count']
                amount=l['metric']['amount']
                tp_tr['State'].append(i)
                tp_tr['Year'].append(j)
                tp_tr['Quarter'].append(int(k.strip('.json')))
                tp_tr['District_name'].append(dt_name)
                tp_tr['Count'].append(count)
                tp_tr['Amount'].append(amount)
            for m in top_tr_data['data']['pincodes']:
                pincode = l['entityName']
                pincode_count = l['metric']['count']
                pincode_amount = l['metric']['amount']
                tp_trp['State'].append(i)
                tp_trp['Year'].append(j)
                tp_trp['Quarter'].append(int(k.strip('.json')))
                tp_trp['Pincodes'].append(pincode)
                tp_trp['Pincode_count'].append(pincode_count)
                tp_trp['Pincode_amount'].append(pincode_amount)
tr_tp_df=pd.DataFrame(tp_tr)
trp_tp_df=pd.DataFrame(tp_trp)

tp_usr_st_path=r'C:\Users\Vinoth\PycharmProjects\PhonepePulse\pulse\data\top\user\country\india\state'
tp_usr_st_list=os.listdir(tp_usr_st_path)
tp_usr={'State': [], 'Year': [], 'Quarter': [],'District_name':[], 'RegisteredUsers':[]}
tp_usrp={'State': [], 'Year': [], 'Quarter': [],'Pincodes':[],'RegisteredUsers':[]}
for i in tp_usr_st_list:
    tp_usr_st_yr_path=tp_usr_st_path+'/'+i
    tp_usr_st_yr_list=os.listdir(tp_usr_st_yr_path)
    for j in tp_usr_st_yr_list:
        tp_usr_st_yr_file_path=tp_usr_st_yr_path+'/'+j
        tp_usr_st_yr_file_list=os.listdir(tp_usr_st_yr_file_path)
        for k in tp_usr_st_yr_file_list:
            file = tp_usr_st_yr_file_path + '/' + k
            data = open(file, 'r')
            top_usr_data = json.load(data)
            for l in top_usr_data['data']['districts']:
                name=l['name']
                registeredUsers=l['registeredUsers']
                tp_usr['State'].append(i)
                tp_usr['Year'].append(j)
                tp_usr['Quarter'].append(int(k.strip('.json')))
                tp_usr['District_name'].append(name)
                tp_usr['RegisteredUsers'].append(registeredUsers)
            for m in top_usr_data['data']['pincodes']:
                name=m['name']
                tp_usrp['State'].append(i)
                tp_usrp['Year'].append(j)
                tp_usrp['Quarter'].append(int(k.strip('.json')))
                tp_usrp['Pincodes'].append(name)
                tp_usrp['RegisteredUsers'].append(registeredUsers)
usr_tp_df=pd.DataFrame(tp_usr)
usrp_tp_df=pd.DataFrame(tp_usrp)






