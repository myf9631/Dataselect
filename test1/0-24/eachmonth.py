import os
import numpy as np
from testtest import Selectdata


month_num = ('201811', '201812', '201901', '201902' )

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
                # row = 13
                list_shape =48
                each_month.eachfiles(monthpath,list_shape)
            elif month == '201902':  # 20192月 17号晚8点结束
                # row = 7
                list_shape=34
                each_month.eachfiles(monthpath, list_shape)
            elif month == '201901':  # 20191月 1-4号 21-31号
                # row = 7
                list_shape=24  #原来是30 ，由于缺失了23、24、28号的数据，故改为24
                each_month.eachfiles(monthpath, list_shape)
            else:
                list_shape=62
                each_month.eachfiles(monthpath, list_shape)
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
    np.save(file="data0-24_EC_20181107-20190217.npy", arr=a)
    print('数据保存成功')


eachmonth('H:\\')
