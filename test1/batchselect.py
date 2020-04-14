# -*- coding: utf-8
# 读文件
import os

# 处理文件数量
count = 0


def readFile(filepath):
    f1 = open(filepath, "r")
    nowDir = os.path.split(filepath)[0]  # 获取路径中的父文件夹路径
    fileName = os.path.split(filepath)[1]  # 获取路径中文件名
    nowDirs = os.path.join('H:\\newData\\201810\\rain12', '999')
    WorldDataDir = os.path.join(nowDirs, "new_" + fileName)  # 对新生成的文件进行命名的过程
    f_world = open(WorldDataDir, "w")  # 对新生成的文件打开写入内容
    lines = f1.readlines()  # 读出原文件的内容 ，读出的是list
    for line in lines[125:173]:
        if line == '\n':
            continue
        temp = line
        if temp in lines[125:173]:
            temp = temp.strip().split('\t')
            temp = temp[68:92]
            temp = ' '.join(temp)
            # print(temp)
            f_world.write(temp + '\n')
    f1.close()
    f_world.close()

    global count
    count += 1


def eachFile(filepath):
    pathDir = os.listdir(filepath)  # 获取当前路径下的文件名，返回List
    for s in pathDir:
        newDir = os.path.join(filepath, s)  # 将文件命加入到当前文件路径后面
        if os.path.isfile(newDir):  # 如果是文件
            readFile(newDir)  # 读文件
            pass
        else:
            eachFile(newDir)  # 如果不是文件，递归这个文件夹的路径


eachFile("H:\\201810\\ecmwf_thin\\rain12")
print("共处理%d个文件" % int(count))
