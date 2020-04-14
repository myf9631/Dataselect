#- * - coding: gb2312 -*-

import numpy as  np
import pandas as pd
from pandas._config import display

#不以科学计数法表示
np.set_printoptions(suppress=True)

#原始数表 34个特征
data= np.load('data_EC_20181107-20190228.npy')
#目标值
y = np.load('data_2d_yundingtotalobs_qiwen_2018110708-20190228.npy')
target = y.reshape(3224, -1)
print(data.shape)
print(y.shape)
#print(data)

#得到34个特征
x1 = data[0,:,:]
#print(x1.shape)
feature1 = x1.reshape(3224, -1)
x2 = data[1,:,:]
feature2 = x2.reshape(3224, -1)
x3 = data[2,:,:]
feature3 = x3.reshape(3224, -1)
x4 = data[3,:,:]
feature4 = x4.reshape(3224, -1)
x5 = data[4,:,:]
feature5 = x5.reshape(3224, -1)
x6 = data[5,:,:]
feature6 = x6.reshape(3224, -1)
x7 = data[6,:,:]
feature7 = x7.reshape(3224, -1)
x8 = data[7,:,:]
feature8 = x8.reshape(3224, -1)
x9 = data[8,:,:]
feature9 = x9.reshape(3224, -1)
x10 = data[9,:,:]
feature10 = x10.reshape(3224, -1)
x11 = data[10,:,:]
feature11 = x11.reshape(3224, -1)
x12 = data[11,:,:]
feature12 = x12.reshape(3224, -1)
x13 = data[12,:,:]
feature13 = x13.reshape(3224, -1)
x14 = data[13,:,:]
feature14 = x14.reshape(3224, -1)
x15 = data[14,:,:]
feature15 = x15.reshape(3224, -1)
x16 = data[15,:,:]
feature16 = x16.reshape(3224, -1)
x17 = data[16,:,:]
feature17 = x17.reshape(3224, -1)
x18 = data[17,:,:]
feature18 = x18.reshape(3224, -1)
x19 = data[18,:,:]
feature19 = x19.reshape(3224, -1)
x20 = data[19,:,:]
feature20 = x20.reshape(3224, -1)
x21 = data[20,:,:]
feature21 = x21.reshape(3224, -1)
x22 = data[21,:,:]
feature22 = x22.reshape(3224, -1)
x23 = data[22,:,:]
feature23 = x23.reshape(3224, -1)
x24 = data[23,:,:]
feature24 = x24.reshape(3224, -1)
x25 = data[24,:,:]
feature25 = x25.reshape(3224, -1)
x26 = data[25,:,:]
feature26 = x26.reshape(3224, -1)
x27 = data[26,:,:]
feature27 = x27.reshape(3224, -1)
x28 = data[27,:,:]
feature28 = x28.reshape(3224, -1)
x29 = data[28,:,:]
feature29 = x29.reshape(3224, -1)
x30 = data[29,:,:]
feature30 = x30.reshape(3224, -1)
x31 = data[30,:,:]
feature31 = x31.reshape(3224, -1)
x32 = data[31,:,:]
feature32 = x32.reshape(3224, -1)
x33 = data[32,:,:]
feature33 = x33.reshape(3224, -1)
x34 = data[33,:,:]
feature34 = x34.reshape(3224, -1)

 #水平拼接
feature_target = np.hstack((feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,
                     feature11,feature12,feature13,feature14,feature15,feature16,feature17,feature18,feature19,feature20,
                     feature21, feature22, feature23, feature24, feature25, feature26, feature27, feature28, feature29,
                     feature30,feature31, feature32, feature33, feature34,target))
# 准备数据
data1 = feature_target
print(data1.shape)
#print(data_df1)
np.save('20181107-20190228.npy',data1)


