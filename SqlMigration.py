import pandas as pd

from DataCollection import usr_tp_df, usrp_tp_df, trp_tp_df, tr_tp_df, usr_map_df, tr_map_df, usr_ag_df, ag_tr_df
from DataProcessingForAllIndiaAggregatedTransaction import aggregated_all_india_transaction_df
from DataProcessingForAllIndiaAggregatedUser import aggregated_all_india_user_df
from DataProcessingForAllIndiaMapTransaction import map_all_india_transaction_df
from DataProcessingForAllIndiaMapUser import map_all_india_usr_df
from DataProcessingForAllIndiaTopTransaction import topdata_all_india_transaction_df, \
    topdata_all_india_transaction_district_df, topdata_all_india_transaction_pincode_df
from DataProcessingForAllIndiaTopUser import topdata_all_india_user_df, topdata_all_india_user_district_df, \
    topdata_all_india_user_pincodes_df
import mysql.connector

usr_tp_df
usrp_tp_df
trp_tp_df
tr_tp_df
usr_map_df
tr_map_df
usr_ag_df
ag_tr_df
aggregated_all_india_transaction_df
aggregated_all_india_user_df
map_all_india_transaction_df
map_all_india_usr_df
topdata_all_india_transaction_df
topdata_all_india_transaction_district_df
topdata_all_india_user_df
topdata_all_india_user_district_df
topdata_all_india_user_pincodes_df
topdata_all_india_transaction_pincode_df
connection=mysql.connector.connect(host='localhost',user='root',password='root')
mycursor = connection.cursor()
mycursor.execute("CREATE DATABASE if not exists phonepepulse")
mycursor.execute("use phonepepulse")
for i in usr_tp_df.iloc:
    tp=list(i)
    tp[2]=int(tp[2])
    tp[4] = int(tp[4])
    mycursor.execute("Create Table if not exists usr_tp_df(State varchar(255),Year varchar(255), Quarter BIGINT, District_name varchar(255), RegisteredUsers BIGINT)")
    sql='INSERT into usr_tp_df(State, Year, Quarter, District_name, RegisteredUsers)values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql,tp)

for i in usrp_tp_df.iloc:
    tp = list(i)
    tp[2] = int(tp[2])
    tp[4] = int(tp[4])
    mycursor.execute(
        "Create Table if not exists usrp_tp_df(State varchar(255),Year varchar(255), Quarter BIGINT, Pincodes varchar(255), RegisteredUsers BIGINT)")
    sql = 'INSERT into usrp_tp_df(State, Year, Quarter, Pincodes, RegisteredUsers)values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)


for i in trp_tp_df.iloc:
    tp = list(i)
    tp[2] = int(tp[2])
    tp[4] = int(tp[4])
    tp[5] = float(tp[5])
    mycursor.execute(
        "Create Table if not exists trp_tp_df(State varchar(255),Year varchar(255), Quarter BIGINT, Pincodes varchar(255), Pincode_count BIGINT, Pincode_amount float)")
    sql = 'INSERT into trp_tp_df(State, Year, Quarter, Pincodes, Pincode_count, Pincode_amount)values(%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)

for i in tr_tp_df.iloc:
    tp = list(i)
    tp[2] = int(tp[2])
    tp[4] = int(tp[4])
    tp[5] = float(tp[5])
    mycursor.execute(
        "Create Table if not exists tr_tp_df(State varchar(255),Year varchar(255), Quarter BIGINT, District_name varchar(255), Count BIGINT, Amount float)")
    sql = 'INSERT into tr_tp_df(State, Year, Quarter, District_name, Count, Amount)values(%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)


for i in usr_map_df.iloc:
    tp = list(i)
    tp[2] = int(tp[2])
    tp[4] = int(tp[4])
    tp[5] = int(tp[5])
    mycursor.execute(
        "Create Table if not exists usr_map_df(State varchar(255),Year varchar(255), Quarter BIGINT, District_name varchar(255), RegisteredUsers BIGINT, AppOpens BIGINT)")
    sql = 'INSERT into usr_map_df(State, Year, Quarter, District_name, RegisteredUsers, AppOpens)values(%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)


for i in usr_map_df.iloc:
    tp = list(i)
    tp[2] = int(tp[2])
    tp[4] = int(tp[4])
    tp[5] = float(tp[5])
    mycursor.execute(
        "Create Table if not exists tr_map_df(State varchar(255),Year varchar(255), Quarter BIGINT, District_name varchar(255), Transaction_count BIGINT, Transaction_amount float)")
    sql = 'INSERT into tr_map_df(State, Year, Quarter, District_name, Transaction_count, Transaction_amount)values(%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)

for i in usr_ag_df.iloc:
    tp = list(i)
    tp[2] = int(tp[2])
    tp[4] = int(tp[4])
    tp[5] = float(tp[5])
    mycursor.execute(
        "Create Table if not exists usr_ag_df(State varchar(255),Year varchar(255), Quarter BIGINT, Brands varchar(255), UsrCount BIGINT, Percentage float)")
    sql = 'INSERT into usr_ag_df(State, Year, Quarter, Brands, UsrCount, Percentage)values(%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)

for i in ag_tr_df.iloc:
    tp = list(i)
    tp[2] = int(tp[2])
    tp[4] = int(tp[4])
    tp[5] = float(tp[5])
    mycursor.execute(
        "Create Table if not exists ag_tr_df(State varchar(255),Year varchar(255), Quarter BIGINT, Transaction_type varchar(255), Transaction_count BIGINT, Transaction_amount float)")
    sql = 'INSERT into ag_tr_df(State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount)values(%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)


for i in aggregated_all_india_transaction_df.iloc:
    tp = list(i)
    tp[1] = int(tp[1])
    tp[3] = int(tp[3])
    tp[4] = int(tp[4])
    mycursor.execute(
        "Create Table if not exists aggregated_all_india_transaction_df(Year varchar(255), Quarter BIGINT, Category varchar(255), Amount BIGINT, Count BIGINT)")
    sql = 'INSERT into aggregated_all_india_transaction_df(Year, Quarter, Category, Amount, Count)values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)

for i in aggregated_all_india_user_df.iloc:
    tp = list(i)
    tp[1] = int(tp[1])
    tp[2] = int(tp[2])
    tp[3] = int(tp[3])
    mycursor.execute(
        "Create Table if not exists aggregated_all_india_user_df(Year varchar(255), Quarter BIGINT, RegisteredUsers BIGINT, AppOpens BIGINT)")
    sql = 'INSERT into aggregated_all_india_user_df(Year, Quarter, RegisteredUsers, AppOpens)values(%s,%s,%s,%s)'
    mycursor.execute(sql, tp)

for i in map_all_india_transaction_df.iloc:
    tp = list(i)
    tp[1] = int(tp[1])
    tp[3] = int(tp[3])
    tp[4] = int(tp[4])
    mycursor.execute(
        "Create Table if not exists map_all_india_transaction_df(Year varchar(255), Quarter BIGINT, Name varchar(255), Count BIGINT, Amount BIGINT)")
    sql = 'INSERT into map_all_india_transaction_df(Year, Quarter, Name, Count, Amount)values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)


for i in map_all_india_usr_df.iloc:
    tp = list(i)
    tp[1] = int(tp[1])
    tp[3] = int(tp[3])
    tp[4] = int(tp[4])
    mycursor.execute(
        "Create Table if not exists map_all_india_usr_df(Year varchar(255), Quarter BIGINT, StateName varchar(255), RegisteredUsers BIGINT, AppOpens BIGINT)")
    sql = 'INSERT into map_all_india_usr_df(Year, Quarter, StateName, RegisteredUsers, AppOpens)values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)


for i in topdata_all_india_transaction_df.iloc:
    tp = list(i)
    tp[1] = int(tp[1])
    tp[3] = int(tp[3])
    tp[4] = int(tp[4])
    mycursor.execute(
        "Create Table if not exists topdata_all_india_transaction_df(Year varchar(255), Quarter BIGINT, State_Name varchar(255),Count BIGINT, Amount BIGINT)")
    sql = 'INSERT into topdata_all_india_transaction_df(Year, Quarter, State_Name, Count, Amount)values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)


for i in topdata_all_india_transaction_district_df.iloc:
    tp = list(i)
    tp[1] = int(tp[1])
    tp[3] = int(tp[3])
    tp[4] = float(tp[4])
    mycursor.execute(
        "Create Table if not exists topdata_all_india_transaction_district_df(Year varchar(255), Quarter BIGINT, District_name varchar(255), Count BIGINT, Amount float)")
    sql = 'INSERT into topdata_all_india_transaction_district_df(Year, Quarter, District_name, Count, Amount)values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)


for i in topdata_all_india_user_df.iloc:
    tp = list(i)
    tp[1] = int(tp[1])
    tp[3] = int(tp[3])

    mycursor.execute(
        "Create Table if not exists topdata_all_india_user_df(Year varchar(255), Quarter BIGINT, State_Name varchar(255), RegisteredUsers BIGINT)")
    sql = 'INSERT into topdata_all_india_user_df(Year, Quarter, State_Name, RegisteredUsers)values(%s,%s,%s,%s)'
    mycursor.execute(sql, tp)

for i in topdata_all_india_user_district_df.iloc:
    tp = list(i)
    tp[1] = int(tp[1])
    tp[3] = int(tp[3])

    mycursor.execute(
        "Create Table if not exists topdata_all_india_user_district_df(Year varchar(255), Quarter BIGINT, District_name varchar(255), RegisteredUsers BIGINT)")
    sql = 'INSERT into topdata_all_india_user_district_df(Year, Quarter, District_name, RegisteredUsers)values(%s,%s,%s,%s)'
    mycursor.execute(sql, tp)


for i in topdata_all_india_user_pincodes_df.iloc:
    tp = list(i)
    tp[1] = int(tp[1])
    tp[3] = int(tp[3])

    mycursor.execute(
        "Create Table if not exists topdata_all_india_user_pincodes_df(Year varchar(255), Quarter BIGINT, Pincodes varchar(255), RegisteredUsers BIGINT)")
    sql = 'INSERT into topdata_all_india_user_pincodes_df(Year, Quarter, Pincodes, RegisteredUsers)values(%s,%s,%s,%s)'
    mycursor.execute(sql, tp)

for i in topdata_all_india_transaction_pincode_df.iloc:
    tp = list(i)
    tp[1] = int(tp[1])
    tp[3] = int(tp[3])
    tp[4] = float(tp[4])

    mycursor.execute(
        "Create Table if not exists topdata_all_india_transaction_pincode_df(Year varchar(255), Quarter BIGINT, Pincodes varchar(255), Count BIGINT, Amount BIGINT)")
    sql = 'INSERT into topdata_all_india_transaction_pincode_df(Year, Quarter, Pincodes, Count, Amount)values(%s,%s,%s,%s,%s)'
    mycursor.execute(sql, tp)
