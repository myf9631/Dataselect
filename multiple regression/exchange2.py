#- * - coding: gb2312 -*-

import pandas as pd

data_df3= pd.read_csv('20181107-20190228.csv',index_col=0)
# 删除包含0的行
data_df3 = data_df3[(data_df3['8'] > 0) & (data_df3['34'] != 0)]
#data_train = data_train.replace({0:np.nan}).fillna(data_train.median())
print(data_df3.shape)
print(data_df3)
# data_df3.drop(columns=['Unnamed: 0'])
# a=data_df3.columns.values.tolist()
# print(a)
# print(data_df3)
data_df3.to_csv('dropzero_20181107-20190228.csv')