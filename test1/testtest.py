# 云顶一号站 经度：115.42	纬度：40.95972222  海拔高速：1923.4
import os
import numpy as np
import json
import h5py

# date_list = [[] for row in range(34)]  # 46代表46个属性

foretime_step = (
    '000', '003', '006', '009', '012', '015', '018', '021', '024', '027', '030', '033', '036', '039', '042', '045',
    '048', '051', '054', '057', '060', '063', '066', '069', '072')  # 预测步长
forcast_element_0 = (
    '2D', '2T', '10u', '10uv', '10v', 'LCC', 'SKT', 'TCC', 'TP')  # 取第74行（152），84列 105-125_50-30_0.125_161
forcast_element_1 = ('Q', 'T', 'R', 'uv')  # 取第38行（80），42列  105-125_50-30_0.25_81
forcast_element_2 = ('MSL', 'SP')  # 取第150行（314），205列  90-130_60-25_0.125_321_281
forcast_element_3 = ('MX2T3', 'MN2T3', '10FG3')  # 105-125_50-30_0.125_161 无.000


class Selectdata():
    def __init__(self):
        self.array_eachelement_date_0 = []
        self.array_eachelement_date_1 = []  # 列表
        self.array_eachelement_date_2 = []
        self.data_list = []

    def element_0_file(self, filepath, temp):
        pathdir = os.listdir(filepath)  # 该路径下的所有文件名
        i = 0  # i 列 表示一天的预测步长
        global list_eachelement_date
        list_eachelement_date = [[0 for i in range(0, 26)] for row in range(62)]  # 用来存储单一站点11月7号到1130号的数据
        row = temp
        flag = 0
        for s in pathdir:
            date = s.split('.')[0]  # 日期
            foretime = s.split('.')[1]  # 取出预测步长
            if flag == 0 and foretime in foretime_step:
                list_eachelement_date[row][i] = date
                i += 1
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
                    list_eachelement_date[row][i] = temp  # 将目标数放入列表中
                    i += 1
                    if i >= 26:
                        row += 1
                        i = 0
                        flag = 0
                    break
        self.array_eachelement_date_0 = np.array(list_eachelement_date)  # 将列表转化成数组
        self.data_list.append(self.array_eachelement_date_0)
        # print(list_eachelement_date)
        # print(self.data_list)
        # print(np.array(self.data_list).shape)

    def element_1_file(self, filepath, temp):
        pathdir = os.listdir(filepath)  # 该路径下的所有文件名
        i = 0  # i表示一天的预测步长
        row = temp
        flag = 0
        global list_eachelement_date
        list_eachelement_date = [[0 for i in range(0, 26)] for row in range(62)]  # 用来存储单一站点11月7号到1130号的数据
        for s in pathdir:
            date = s.split('.')[0]  # 日期
            foretime = s.split('.')[1]  # 取出预测步长
            if flag == 0 and foretime in foretime_step:
                list_eachelement_date[row][i] = date
                i += 1
                flag = 1
            if foretime in foretime_step:
                newdir = os.path.join(filepath, s)
                f1 = open(newdir, 'r')
                lines = f1.readlines()  # 读取文件中的所有行 列表
                for line in lines[80:]:  # 取出第74行  此时line为字符串
                    if line == '\n':
                        continue
                    line = line.strip().split('\t')  # 转换成列表的形式
                    temp = line[42]  # 取出第84个
                    list_eachelement_date[row][i] = temp  # 将目标数放入列表中
                    i += 1
                    if i >= 26:
                        row += 1
                        i = 0
                        flag = 0
                    break
        self.array_eachelement_date_1 = np.array(list_eachelement_date)  # 将列表转化成数组
        self.data_list.append(self.array_eachelement_date_1)
        # print(self.data_list)
        # print(np.array(self.data_list).shape)

    def element_2_file(self, filepath, temp):
        pathdir = os.listdir(filepath)  # 该路径下的所有文件名
        i = 0  # i表示一天的预测步长
        row = temp
        flag = 0
        global list_eachelement_date
        list_eachelement_date = [[0 for i in range(0, 26)] for row in range(62)]  # 用来存储单一站点11月7号到1130号的数据
        for s in pathdir:
            date = s.split('.')[0]  # 日期
            foretime = s.split('.')[1]  # 取出预测步长
            if flag == 0 and foretime in foretime_step:
                list_eachelement_date[row][i] = date
                i += 1
                flag = 1
            if foretime in foretime_step:
                newdir = os.path.join(filepath, s)
                f1 = open(newdir, 'r')
                lines = f1.readlines()  # 读取文件中的所有行 列表
                for line in lines[314:]:  # 取出第74行  此时line为字符串
                    if line == '\n':
                        continue
                    line = line.strip().split('\t')  # 转换成列表的形式
                    temp = line[205]  # 取出第84个
                    list_eachelement_date[row][i] = temp  # 将目标数放入列表中
                    i += 1
                    if i >= 26:
                        row += 1
                        i = 0
                        flag = 0
                    break
        self.array_eachelement_date_2 = np.array(list_eachelement_date)  # 将列表转化成数组
        self.data_list.append(self.array_eachelement_date_2)
        # print(list_eachelement_date)
        # print(self.data_list)
        # print(np.array(self.data_list).shape)

    def element_3_file(self, filepath, temp):
        pathdir = os.listdir(filepath)  # 该路径下的所有文件名
        i = 0  # i表示一天的预测步长
        row = temp
        flag = 0
        global list_eachelement_date
        list_eachelement_date = [[0 for i in range(0, 26)] for row in range(62)]  # 用来存储单一站点整月的数据
        for s in pathdir:
            date = s.split('.')[0]  # 日期
            foretime = s.split('.')[1]  # 取出预测步长
            if flag == 0 and foretime in foretime_step:
                list_eachelement_date[row][i] = date
                i =2
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
                    list_eachelement_date[row][i] = temp  # 将目标数放入列表中
                    i += 1
                    if i >= 26:
                        row += 1
                        i = 0
                        flag=0
                    break
            # print(list_eachelement_date)
        self.array_eachelement_date_0 = np.array(list_eachelement_date)  # 将列表转化成数组
        self.data_list.append(self.array_eachelement_date_0)
        # print(self.data_list)
        # print(np.array(self.data_list).shape)

    def Out(self):
        # print(self.data_list)
        self.data_array = np.array(self.data_list)  # 列表转成数组
        # self.data_array
        # temp_list =self.data_list
        # np.save(file="data11.npy", arr=self.data_array)
        # f=h5py.File('eachmonth10.h5','w')
        # f['data']=temp_list
        # f['labels'] =self.data_list
        # f.close()

        # filename = 'eachmonth10.json'
        # with open(filename, 'w') as j_obj:
        #     json.dump(temp_list, j_obj)

        return self.data_array

    def eachfiles(self, filespath, row):
        pathdir = os.listdir(filespath)
        j = 0
        for fil in pathdir:
            if fil in forcast_element_0:
                # path = '999\\'
                newdir = os.path.join(filespath, fil, path)
                # print(newdir)
                self.element_0_file(newdir, row)
                # print(data_list)
                j += 1
            if fil in forcast_element_1:
                tempdir = os.path.join(filespath, fil)
                secondir = os.listdir(tempdir)
                hpa_num = ('500', '700', '850', '925', '950')
                for i in hpa_num:
                    intervale = i
                    interpath = intervale + '\\'
                    newdir = os.path.join(tempdir, interpath)
                    # print(newdir)
                    self.element_1_file(newdir, row)
                    # print(data_list)
                    j += 1
            if fil in forcast_element_2:
                path = '999\\'
                newdir = os.path.join(filespath, fil, path)
                # print(newdir)
                self.element_2_file(newdir, row)
                # print(data_list)
                j += 1
            if fil in forcast_element_3:
                path = '999\\'
                newdir = os.path.join(filespath, fil, path)
                # print(newdir)
                self.element_3_file(newdir, row)
                # print(data_list)
                j += 1

# mouth_11 = Selectdata()
# temp = mouth_11.eachfiles('H:\\201811\\ecmwf_thin\\')
# print('云顶一号站 经度：115.42	纬度：40.95972222  海拔高速：1923.4')
# print('三维张量的形状', mouth_11.Out().shape)
# data_dict = {'EC_data': mouth_11}
# print(data_dict['EC_data'])
