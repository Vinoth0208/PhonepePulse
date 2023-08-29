from DataCollection import usr_tp_df, usrp_tp_df, trp_tp_df, usr_map_df, tr_tp_df, tr_map_df, usr_ag_df, ag_tr_df
from DataProcessingForAllIndiaAggregatedTransaction import aggregated_all_india_transaction_df
from DataProcessingForAllIndiaAggregatedUser import aggregated_all_india_user_df
from DataProcessingForAllIndiaMapTransaction import map_all_india_transaction_df
from DataProcessingForAllIndiaMapUser import map_all_india_usr_df
from DataProcessingForAllIndiaTopTransaction import topdata_all_india_transaction_df, \
    topdata_all_india_transaction_district_df, topdata_all_india_transaction_pincode_df
from DataProcessingForAllIndiaTopUser import topdata_all_india_user_district_df, topdata_all_india_user_df, \
    topdata_all_india_user_pincodes_df

usr_tp_df.to_csv(r'Datas\usr_tp_df.csv')
usrp_tp_df.to_csv(r'Datas\usrp_tp_df.csv')
trp_tp_df.to_csv(r'Datas\trp_tp_df.csv')
tr_tp_df.to_csv(r'Datas\tr_tp_df.csv')
usr_map_df.to_csv(r'Datas\usr_map_df.csv')
tr_map_df.to_csv(r'Datas\tr_map_df.csv')
usr_ag_df.to_csv(r'Datas\usr_ag_df.csv')
ag_tr_df.to_csv(r'Datas\ag_tr_df.csv')
aggregated_all_india_transaction_df.to_csv(r'Datas\aggregated_all_india_transaction_df.csv')
aggregated_all_india_user_df.to_csv(r'Datas\aggregated_all_india_user_df.csv')
map_all_india_transaction_df.to_csv(r'Datas\map_all_india_transaction_df.csv')
map_all_india_usr_df.to_csv(r'Datas\map_all_india_usr_df.csv')
topdata_all_india_transaction_df.to_csv(r'Datas\topdata_all_india_transaction_df.csv')
topdata_all_india_transaction_district_df.to_csv(r'Datas\topdata_all_india_transaction_district_df.csv')
topdata_all_india_user_df.to_csv(r'Datas\topdata_all_india_user_df.csv')
topdata_all_india_user_district_df.to_csv(r'Datas\topdata_all_india_user_district_df.csv')
topdata_all_india_user_pincodes_df.to_csv(r'Datas\topdata_all_india_user_pincodes_df.csv')
topdata_all_india_transaction_pincode_df.to_csv(r'Datas\topdata_all_india_transaction_pincode_df.csv')