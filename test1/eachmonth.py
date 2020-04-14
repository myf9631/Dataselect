import os
import numpy as np
from test1.testtest import Selectdata
import json

month_num = ('201811', '201812', '201901', '201902' )

# each_month = Selectdata()

# temp = mouth_11.eachfiles('H:\\201811\\ecmwf_thin\\')
# print(mouth_11.Out().shape)
# data_dict = {'EC_data': mouth_11}
# print(data_dict['EC_data'])
def eachmonth(filepath):
    pathdir = os.listdir(filepath)
    flag = 0
    for month in pathdir:
        if month in month_num:
            path = 'ecmwf_thin\\'
            monthpath = os.path.join(filepath, month, path)  # 'H:\\201811\\ecmwf_thin\\'
            # print(monthpath)
            each_month = Selectdata()
            if month == '201811':  # 201811从7号开始
                row = 13
                each_month.eachfiles(monthpath, row)
            elif month == '201903':  # 20193月从4号开始
                row = 7
                each_month.eachfiles(monthpath, row)
            else:
                row = 0
                each_month.eachfiles(monthpath, row)
            eachmonthdata = each_month.Out()
            if flag == 0:
                a = eachmonthdata
                flag = 1
            else:
                b = eachmonthdata
                a = np.concatenate((a, b), axis=1)
                print(a.shape)
            # total_month.append(each_month.Out())
            # data_dict = {'EC_data': each_month.Out()}
            # print(np.array(total_month).shape)
    np.save(file="./0-72/data0-72_EC_20181107-20190228.npy", arr=a)
    print('数据保存成功')


# print('云顶一号站 经度：115.42	纬度：40.95972222  海拔高速：1923.4')
# print(np.array(a).shape)


eachmonth('H:\\')
