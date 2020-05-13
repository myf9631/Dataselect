import os
import numpy as np
import pandas as pd
import json

#
foretime_step = (
    '000', '003', '006', '009', '012', '015', '018', '021', '024')  # 预测步长


def eachfile(filepath):
    pathdir = os.listdir(filepath)  # 该路径下的所有文件名
    i = 0  # i表示一天的预测步长
    global list_eachelement_date
    list_eachelement_date = [[0 for i in range(0, 26)] for row in range(34)]  # 用来存储单一站点11月7号到1130号的数据
    print(np.array(list_eachelement_date).shape)
    row = 0
    flag = 0
    step = 0
    for s in pathdir:
        date = s.split('.')[0]  # 日期
        foretime = s.split('.')[1]  # 取出预测步长
        if flag == 0 and foretime in foretime_step:  ##加日期
            list_eachelement_date[row][i] = date
            # print(list_eachelement_date)
            i = 1
            flag = 1
        if foretime == foretime_step[step]:
            f1 = open(os.path.join(filepath, s), 'r')
            lines = f1.readlines()  # 读取文件中的所有行 列表
            for line in lines[152:]:  # 取出第74行  此时line为字符串
                if line == '\n':
                    continue
                line = line.strip().split('\t')  # 转换成列表的形式
                temp = line[84]  # 取出第84个
                list_eachelement_date[row][i] = temp  # 将目标数放入列表中
                i += 3
                # print(list_eachelement_date)
                if i >= 26:
                    row += 1
                    i = 0
                    flag = 0
                    # step=0
                break
        if foretime != foretime_step[step] and foretime in foretime_step:
            f1 = open(os.path.join(filepath, s), 'r')
            lines = f1.readlines()  # 读取文件中的所有行 列表
            for line in lines[152:]:  # 取出第74行  此时line为字符串
                if line == '\n':
                    continue
                line = line.strip().split('\t')  # 转换成列表的形式
                temp = line[84]  # 取出第84个
                i += 3
                list_eachelement_date[row][i] = temp  # 将目标数放入列表中
                i += 3
                # print(list_eachelement_date)
                step += 1
                if i >= 26:
                    row += 1
                    i = 0
                    flag = 0
                    step = 0
                break
        step += 1
        if step >= 9:
            step = 0
        if foretime not in foretime_step:
            step = 0
        # print(list_eachelement_date)
    print(list_eachelement_date)
    # print(np.array(list_eachelement_date).shape)


eachfile('H:\\201902\\ecmwf_thin\\2T\\999')

# data=np.load('./0-72/data0-72_EC_20181107-20190228.npy')
# # data=pd.DataFrame(data)
# print(data[0])
