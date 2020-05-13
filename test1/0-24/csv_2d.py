import numpy as np
import pandas as pd
'''
24h逐小时预测，EC时间段为2018110708--2019021720
因此取观测数据中的时间段为2018110808--2019021920
'''

data = pd.read_csv('../hour_data01/yunding1.csv', usecols=['正点气温'], encoding='GBK')
data_20181110_20190223 = data[3699:5800]
data_20181110_20190223.index = range(len(data_20181110_20190223))
data_df = data_20181110_20190223.drop(data_20181110_20190223.index[1456:1504])
data_df.index = range(len(data_df))
# print(data_df)
new_data_df = data_df.drop(data_df.index[1528:1552])
print(new_data_df)

# DataFrame 转为list
data_list = []
for i in range(2029):  # 2149
    # if i % 3 == 0:
        data_df_sp = new_data_df.iloc[[i]]
        # print(data_df_sp)
        i += 1
        citydaima = np.array(data_df_sp)
        # a=citydaima[0]
        a = citydaima[0][0]
        data_list.append(a)
# print(data_list)
print(np.array(data_list).shape)

# 将数据组成二维
# 云顶1号站12月17号缺少数据 已填充
total_data = [[0 for i in range(0, 25)] for row in range(169)]
row = 0
j = 0
i = 0
while i < 2029:  # 821 717
    total_data[row][j] = data_list[i]
    j += 1
    i += 1
    if j > 24:
        row += 1
        j = 0
        i -= 13
    # print(total_data)

for i in range(169):
    print(total_data[i])
print(np.array(total_data).shape)


#
np.save("data0-24_2d_yunding1obs_20181107-20190217.npy", arr=total_data[0:168])
print("数据保存成功")

# print(np.array(data_EC).shape)
# print(data_EC)
