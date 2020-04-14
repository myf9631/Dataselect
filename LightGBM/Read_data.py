#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author：bqq time:2020/4/7
import numpy as np

a = np.load(r'data_EC_20181107-20190228.npy')
b = np.load(r'data_2d_yundingtotalobs_qiwen_2018110708-20190228.npy')
print(a)
print(b)
print('a的维度：', a.shape)
print('b的维度：', b.shape)

A = np.reshape(a, (34, -1))
B = np.reshape(b, (1, -1))
print(A.shape) #（34，,3224）
print(B.shape)

np.savetxt('new_data_EC_20181107-20190228.csv', np.transpose(A),
           delimiter=',', fmt='%s') #（3224,34）
np.savetxt('new_data_2d_yundingtotalobs_qiwen_2018110708-20190228.csv',
           np.transpose(B), delimiter=',', fmt='%s')
