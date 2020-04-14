# 在学习之前，先导入这些常用的模块
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import mglearn
# 导入lasso模块
from sklearn.linear_model import Lasso
# 导入 train_test_split 模块
from sklearn.model_selection import train_test_split

# path = 'G:\\气象数据\\气象预测\\winter_olympic_obs_hourly(1)\\hour_data\\bia1.csv'
# df = pd.read_csv(path)
# X = df.iloc[1:, ].values
# y = df.DataFrame(df, columns=[u"正点气温"])
# # 导入波士顿房价数据
# X, y = mglearn.datasets.load_extended_boston()

# 加载数据，设置浮点型数值
data_features = np.load('data_EC_20181107-20190228.npy')
data_targets = np.load('data_2d_yundingtotalobs_qiwen_2018110708-20190228.npy')
data_features = data_features.astype(float)
data_targets = data_targets.astype(float)
data_targets = np.around(data_targets, decimals=2)
data_features.shape  # （34,248,13）
data_features = data_features.reshape((34, 3224))
data_targets = data_targets.reshape((3224,))
data_all = np.append(data_features, [data_targets], axis=0)  # 34 * 3224
# print(np.array(data_all).shape)
data_all = data_all.transpose()  # 转置3244*35
np.savetxt("./targets.csv", data_all, delimiter=",", fmt="%f")

# 数据清洗
data_csv = pd.read_csv("./targets.csv", header=None)
# 去除特征值全为0的行 和 去除目标值为0的行
data_csv = data_csv.loc[~(data_csv.loc[:, 0:33] == 0).all(axis=1) & ~(data_csv.loc[:, 34] == 0), :]
np.savetxt("./targets1.csv", data_csv, delimiter=",", fmt="%f")

# 将数据分为训练集与测试集
data_csv = pd.read_csv("./targets1.csv", header=None)
features = data_csv.loc[0:1950, 0:33]
trargets = data_csv.loc[0:1950, 34]
X_train, X_test, y_train, y_test = train_test_split(features, trargets)  # 默认样本比例是0.75，0.25

# 实例化lasso对象，并对训练集数据进行训练
lasso = Lasso().fit(X_train, y_train)

print('lasso在训练集的评估分数：', lasso.score(X_train, y_train))
print('lasso在测试集的评估分数：', lasso.score(X_test, y_test))
print('lasso模型保存的特征数量：', np.sum(lasso.coef_ != 0))

plt.plot(lasso.coef_, 's', label='Lasso alpha=1')
# plt.plot(lasso001.coef_, '^', label='Lasso alpha=0.01')
# plt.plot(lasso00001.coef_, 's', label='Lasso alpha=0.0001')

plt.legend(ncol=2, loc=(0, 1.05))
plt.ylim(-25, 25)
plt.xlabel('Coefficient index')
plt.ylabel('Coefficient magnitude')
plt.show()
