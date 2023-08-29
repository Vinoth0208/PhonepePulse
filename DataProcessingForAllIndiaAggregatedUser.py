import json
import os

import pandas as pd

user_path='pulse/data/aggregated/user/country/india'
year_list=os.listdir(user_path)
ag_all_india={'Year': [], 'Quarter': [], 'RegisteredUsers': [], 'AppOpens': []}
for i in range(len(year_list)-1):
    filepath=user_path+'/'+year_list[i]
    filelist=os.listdir(filepath)
    for j in filelist:
        file=filepath+'/'+j
        data=open(file,'r')
        all_india_user_data=json.load(data)
        RegisteredUsers=all_india_user_data['data']['aggregated']['registeredUsers']
        AppOpens=all_india_user_data['data']['aggregated']['appOpens']
        ag_all_india['Year'].append(year_list[i])
        ag_all_india['Quarter'].append(int(j.strip('.json')))
        ag_all_india['RegisteredUsers'].append(RegisteredUsers)
        ag_all_india['AppOpens'].append(AppOpens)

aggregated_all_india_user_df=pd.DataFrame(ag_all_india)



