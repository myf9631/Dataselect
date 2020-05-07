import numpy as np
import pandas as pd

# 2018111820-2019021820
# 云顶1：3711-6172  2461
# 云顶2：3705-6166
# 云顶3：3702-6163
# 云顶4: 3706-61567
# 云顶5:3617-6078
# 云顶6:3718-6179
# 云顶山底：3811-6261
# 云顶山顶3811-6260
# 山腰：3811-6260

# 2018111008--2019022320
# 2018111008--20190107  20190123--2019022320
# yunding1:3747-6280
# 云顶2：3741--6274

data = pd.read_csv('hour_data01/yunding1.csv', usecols=['正点气温'], encoding='GBK')
data_20181110_20190223 = data[3747:5896]
data_20181110_20190223.index = range(len(data_20181110_20190223))
data_df = data_20181110_20190223.drop(data_20181110_20190223.index[1456:1504])
data_df.index = range(len(data_df))
# print(data_df)
new_data_df = data_df.drop(data_df.index[1528:1552])
print(new_data_df)

# 每隔三小时一个数据
data_list = []
for i in range(2077):  # 2149
    if i % 3 == 0:
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
while i < 693:  # 821 717
    total_data[row][j] = data_list[i]
    j += 1
    i += 1
    if j > 24:
        row += 1
        j = 0
        i -= 21

for i in range(169):
    print(total_data[i])
print(np.array(total_data).shape)


#
np.save("./0-72/data0-72_2d_yunding1obs_20181107-20190217.npy", arr=total_data[0:168])
print("数据保存成功")

# print(np.array(data_EC).shape)
# print(data_EC)
