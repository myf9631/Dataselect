# coding=gbk
#导入类库和加载数据集
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame
from sklearn.model_selection import train_test_split

# 读取文件
data = pd.read_csv('dropzero_20181107-20190228.csv')
examDf = DataFrame(data)

# 数据清洗,比如第一列有可能是日期，这样的话我们就只需要从第二列开始的数据，
# 这个情况下，把下面中括号中的0改为1就好，要哪些列取哪些列
new_examDf = examDf.iloc[:, 0:]

# 检验数据
print(new_examDf.describe())  # 数据描述，会显示最值，平均数等信息，可以简单判断数据中是否有异常值
print(new_examDf[new_examDf.isnull() == True].count())  # 检验缺失值，若输出为0，说明该列没有缺失值

# 输出相关系数，判断是否值得做线性回归模型
print(new_examDf.corr())  # 0-0.3弱相关；0.3-0.6中相关；0.6-1强相关；

# 通过seaborn添加一条最佳拟合直线和95%的置信带，直观判断相关关系
sns.pairplot(data, x_vars=['2','5','8'], y_vars= ['34'], size=7, aspect=0.8, kind='reg')
plt.show()


# 拆分训练集和测试集 0.75、0.25
#0-33 一共34个特征 作为自变量x    34列为目标值列
X_train, X_test, Y_train, Y_test = train_test_split(new_examDf.iloc[:, :34], new_examDf.iloc[:,34],
                                                    train_size=0.75,random_state=0)

print("自变量---源数据:", new_examDf.iloc[:, :34].shape, "；  训练集:", X_train.shape, "；  测试集:", X_test.shape)
print("因变量---源数据:", new_examDf.iloc[:,34].shape, "；    训练集:", Y_train.shape, "；  测试集:", Y_test.shape)
# 调用线性规划包
model = LinearRegression()
model.fit(X_train, Y_train)  # 线性回归训练

a = model.intercept_  # 截距
b = model.coef_  # 回归系数

print("拟合参数:截距", a, ",回归系数：", b)

# 显示线性方程，并限制参数的小数位为两位
print("最佳拟合线: Y = ", round(a, 4), "+", round(b[0], 4), "* X1 + ", round(b[1], 4), "* X2 +",
      round(b[2],4),"* X3 + ",round(b[3], 4), "* X4 + ", round(b[4], 4), "* X5","+",round(b[5],4),"* X6 +",
round(b[6],4),"* X7 + ",round(b[7], 4), "* X8 + ", round(b[8], 4), "* X9","+",round(b[9],4), "* X10 +",
round(b[10],4),"* X11 + ",round(b[11], 4), "* X12 + ", round(b[12], 4), "* X13","+",round(b[13],4),"* X14 +",
round(b[14],4),"* X15 + ",round(b[15], 4), "* X16 + ", round(b[16], 4), "* X17","+",round(b[17],4), "* X18 +",
 round(b[18],4),"* X19 + ",round(b[19], 4), "* X20 + ", round(b[10], 4), "* X21","+",round(b[21],4), "* X22 +",
round(b[22],4),"* X23 + ",round(b[23], 4), "* X24 + ", round(b[24], 4), "* X25","+",round(b[25],4), "* X26 +",
round(b[26],4),"* X27 + ",round(b[27], 4), "* X28 + ", round(b[28], 4), "* X29","+",round(b[29],4), "* X30 +",
round(b[30],4),"* X31 + ",round(b[31], 4), "* X32 ",round(b[32],4),"* X33 + ",round(b[33], 4), "* X34 ")

# 对测试集数据，用predict函数预测
Y_pred = model.predict(X_test)

#添加标签画图
plt.figure()
plt.plot(range(len(Y_pred)), Y_pred, 'red', linewidth=2.5, label="predict data")
plt.plot(range(len(Y_test)), Y_test, 'green', label="test data")
plt.show()

plt.figure()
y = Y_pred - Y_test
plt.plot(y)
#图标位于左上角，即第2象限，类似的，1为右上角，3为左下角，4为右下角
plt.legend(loc=2)
plt.show()  # 显示预测值与测试值曲线


#准确性
score = model.score(X_test,Y_test)
print('准确率:',score)