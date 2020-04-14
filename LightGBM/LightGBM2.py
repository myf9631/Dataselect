from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

## 加载数据
# iris = load_iris()
# data = iris.data
# target = iris.target
#
# 加载你的数据
# my_matrix = np.loadtxt(open(r'new_data.csv'), delimiter=",", skiprows=0)
# features, targets = my_matrix[:, :-1], my_matrix[:, -1]
# 晓梦数据
data = pd.read_csv('dropzero_20181107-20190228.csv')
examDf = DataFrame(data)
new_examDf = examDf.iloc[:, 0:]

# # 检验数据
# print(new_examDf.describe())  # 数据描述，会显示最值，平均数等信息，可以简单判断数据中是否有异常值
# print(new_examDf[new_examDf.isnull() == True].count())  # 检验缺失值，若输出为0，说明该列没有缺失值


# 划分训练数据和测试数据
# X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2)

# X_train,X_test,y_train,y_test = train_test_split(features,targets,test_size=0.25)

#晓梦
X_train, X_test, y_train, y_test = train_test_split(new_examDf.iloc[:, :34], new_examDf.iloc[:, 34],
                                                    train_size=0.75, random_state=0)

# 模型训练
gbm = LGBMRegressor(objective='regression', num_leaves=31, learning_rate=0.1, n_estimators=40)
gbm.fit(X_train, y_train, eval_set=[(X_test, y_test)], eval_metric='l1', early_stopping_rounds=5)

# 模型存储
joblib.dump(gbm, 'loan_model.pkl')
# 模型加载
gbm = joblib.load('loan_model.pkl')

# 模型预测
y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration_)

# 模型评估
print('The rmse of prediction is:', mean_squared_error(y_test, y_pred) ** 0.5)

# 特征重要度
print('Feature importances:', list(gbm.feature_importances_))

# 网格搜索，参数优化
estimator = LGBMRegressor(num_leaves=31)
param_grid = {
    'learning_rate': [0.01, 0.1, 1],
    'n_estimators': [20, 40]
}
gbm = GridSearchCV(estimator, param_grid)
gbm.fit(X_train, y_train)
print('Best parameters found by grid search are:', gbm.best_params_)

# regressor = LGBMRegressor()
gbm_score =gbm.score(X_test, y_test)
print('准确率：', gbm_score)


#添加标签画图
plt.figure()
plt.plot(range(len(y_pred)), y_pred, 'red', linewidth=2.5, label="predict data")
plt.plot(range(len(y_test)), y_test, 'green', label="test data")
plt.show()

plt.figure()
y = y_pred - y_test
plt.plot(y)
#图标位于左上角，即第2象限，类似的，1为右上角，3为左下角，4为右下角
plt.legend(loc=2)
plt.show()  # 显示预测值与测试值曲线
