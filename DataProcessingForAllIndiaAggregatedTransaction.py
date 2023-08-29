import json
import os

import pandas as pd

transaction_path='pulse/data/aggregated/transaction/country/india'
year_list=os.listdir(transaction_path)
ag_all_india={'Year': [], 'Quarter': [], 'Category': [], 'Amount': [], 'Usercount': []}
for i in range(len(year_list)-1):
    filepath=transaction_path+'/'+year_list[i]
    filelist=os.listdir(filepath)
    for j in filelist:
        file=filepath+'/'+j
        data=open(file,'r')
        all_india_trancsaction_data=json.load(data)
        for k in all_india_trancsaction_data['data']['transactionData']:
            category=k['name']
            amount=k['paymentInstruments'][0]['amount']
            usercount=k['paymentInstruments'][0]['count']
            ag_all_india['Year'].append(year_list[i])
            ag_all_india['Quarter'].append(int(j.strip('.json')))
            ag_all_india['Category'].append(category)
            ag_all_india['Amount'].append(int(amount))
            ag_all_india['Usercount'].append(usercount)
aggregated_all_india_transaction_df=pd.DataFrame(ag_all_india)


