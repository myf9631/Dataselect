# 根据模式数据的日期，是从2018117号8点开始的数据，
# 因此要选择2018117号8点-20190228结束进行参照.
# 目前拥有模式数据201810到201904的数据

import pandas as pd
import numpy as np

# 云顶1号  3676：6371
# 云顶2号 3676:6370
# 云顶3号 3666:6362
# 云顶4 3670:6366
# 云顶5 3581:6277
# 云顶6 3682:6378
# 78910 没有11月的数据
# yunding_shandi 3775:6471
# yunding_shanding  yanding_shanyao 3775:6471

data = pd.read_csv('hour_data01/yunding1.csv', usecols=['观测时间', '正点气温'])
data_20181101_20190314 = data[3676:6371]
data_20181101_20190314.index = range(len(data_20181101_20190314)) # 从0开始重新排序
data_list = data_20181101_20190314.values.tolist()  # 转换成列表的格式

# print(data_list)
# print(np.array(data_list).shape)

total_data = []
i = 0
for i in range(len(data_list)):
    if i % 3 == 0:
        a = data_list[i]
        # print(a)
        total_data.append(a)
        i += 3
print(total_data)
# np.save('data_yunding1obs_2018110708-20190228',total_data)
print(np.array(total_data).shape)


total_data_list = [[] for row in range(248)]
print(np.array(total_data_list).shape)
i = 0
row = 0
j = 0
# for j in range(13):
for i in range(899):
    # if i % 2 == 0:
    if i >= 13:
        row += 1
        i = 0
    a = total_data[i]
    total_data_list[row].append(a)
    i += 1
    #     j += 1
    print(total_data_list)
