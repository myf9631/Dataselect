#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author：bqq time:2020/4/8
import numpy as np
from sklearn.model_selection import train_test_split
my_matrix = np.loadtxt(open(r'new_data.csv'), delimiter=",", skiprows=0)
X, y = my_matrix[:, :-1], my_matrix[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
train = np.column_stack((X_train, y_train))
np.savetxt('train_usual.csv', train, delimiter=',')
test = np.column_stack((X_test, y_test))
np.savetxt('test_usual.csv', test, delimiter=',')

