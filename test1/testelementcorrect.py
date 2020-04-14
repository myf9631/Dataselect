import os
import numpy as np
import pandas as pd
import json
#
foretime_step = ('000', '003', '006', '009', '012', '015', '018', '021', '024', '027', '030', '033', '036', '039', '042', '045',
    '048', '051', '054', '057', '060', '063', '066', '069', '072')  # 预测步长


# num = [[0 for i in range(1,5)]for j in range(1,5)]
def eachfile(filepath):
    pathdir = os.listdir(filepath)  # 该路径下的所有文件名
    i = 0  # i表示一天的预测步长
    global list_eachelement_date
    list_eachelement_date = [[0 for i in range(0, 26)] for row in range(64)]  # 用来存储单一站点11月7号到1130号的数据
    print(np.array(list_eachelement_date).shape)
    # for row in range(64):
    # array_eachelement_date[row][i].append(0)
    # for i in range(1,13):
    row = 0
    flag=0
    for s in pathdir:
        date = s.split('.')[0]  # 日期
        foretime = s.split('.')[1]  # 取出预测步长
        if flag == 0 and foretime in foretime_step:
            list_eachelement_date[row][i] = date
            i=2
            flag = 1
        if foretime in foretime_step:
            newdir = os.path.join(filepath, s)
            f1 = open(newdir, 'r')
            lines = f1.readlines()  # 读取文件中的所有行 列表

            for line in lines[152:]:  # 取出第74行  此时line为字符串
                if line == '\n':
                    continue
                line = line.strip().split('\t')  # 转换成列表的形式
                temp = line[84]  # 取出第84个
                # list_eachelement_date[i].append(0)
                list_eachelement_date[row][i] = temp  # 将目标数放入列表中
                # print(array_eachelement_date)
                i += 1
                # print(list_eachelement_date)
                if i >= 26:
                    row += 1
                    i = 0
                    flag=0
                break
        print(list_eachelement_date)
    print(list_eachelement_date)
    print(np.array(list_eachelement_date).shape)


eachfile('H:\\201811\\ecmwf_thin\\10FG3\\999')

# data=np.load('./0-72/data0-72_EC_20181107-20190228.npy')
# # data=pd.DataFrame(data)
# print(data[0])