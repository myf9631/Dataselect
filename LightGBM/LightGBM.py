#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author：bqq time:2020/4/2
# coding: utf-8
# pylint: disable = invalid-name, C0111

# 函数的更多使用方法参见LightGBM官方文档：http://lightgbm.readthedocs.io/en/latest/Python-Intro.html

import json
from pyexpat import model

import matplotlib.pyplot as plt
import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, roc_auc_score, explained_variance_score
from sklearn.metrics import accuracy_score


# 加载你的数据
print('Load data...')
df_train = pd.read_csv(r'train_usual.csv', header=None)
df_test = pd.read_csv(r'test_usual.csv', header=None)

X_train = df_train.drop(34, axis=1).values
y_train = df_train[34].values
X_test = df_test.drop(34, axis=1).values
y_test = df_test[34].values



# 创建成lgb特征的数据集格式
lgb_train = lgb.Dataset(X_train, y_train)  # 将数据保存到LightGBM二进制文件将使加载更快
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)  # 创建验证数据

# 将参数写成字典下形式
params = {
    'task': 'train',
    'boosting_type': 'gbdt',  # 设置提升类型
    'objective': 'regression',  # 目标函数
    'metric': {'l2', 'auc'},  # 评估函数
    'num_leaves': 31,  # 叶子节点数
    'learning_rate': 1,  # 学习速率
    'feature_fraction': 0.9,  # 建树的特征选择比例
    'bagging_fraction': 0.8,  # 建树的样本采样比例
    'bagging_freq': 5,  # k 意味着每 k 次迭代执行bagging
    'verbose': 1  # <0 显示致命的, =0 显示错误 (警告), >0 显示信息
}

print('Start training...')
# 训练 cv and train
gbm = lgb.train(params, lgb_train, num_boost_round=20, valid_sets=lgb_eval, early_stopping_rounds=5)  # 训练数据需要参数列表和数据集

print('Save model...')

gbm.save_model('model.txt')  # 训练后保存模型到文件

print('Start predicting...')
# 预测数据集
y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)  # 如果在训练期间启用了早期停止，可以通过best_iteration方式从最佳迭代中获得预测
# 评估模型

print('The difference of prediction is:', y_pred - y_test)
print('The rmse of prediction is:', mean_squared_error(y_test, y_pred) ** 0.5)  # 计算真实值和预测值之间的均方根误差
# score = model.score(X_test, y_test)

y_pred = np.reshape(y_pred, (y_pred.shape[0]))
y_test = np.reshape(y_test, (y_test.shape[0]))

# 画图对比
x = range(len(X_test))
plt.plot(x, y_test, color='green', label='truth')
plt.plot(x, y_pred, color='red', label='prediction')
# a=y_test-y_pred
# plt.plot(a)
plt.legend()
plt.show()

