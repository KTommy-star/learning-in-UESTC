# load_boston 函数在 scikit-learn 1.2 版本后被移除，所以会报错，这里用加利福尼亚的数据集（这里请教了AI）
# 而且画出来效果有点蒙圈
import numpy as np1
import matplotlib.pyplot as plt1
from sklearn.datasets import fetch_california_housing # 加利福尼亚
from sklearn.linear_model import LinearRegression
# 加载数据集
housing = fetch_california_housing()
X = housing.data #定义变量x
y = housing.target #定义变量y

# 选择一个特征进行分析
selected_feature = 'MedInc'  # 在此举例：家庭收入中位数
X_feature = housing.data[:, housing.feature_names.index(selected_feature)]
# 创建线性回归模型
model2 = LinearRegression()

# 拟合模型
model2.fit(X_feature.reshape(-1, 1), y)
# 使用模型进行预测
X_new2 = np1.linspace(X_feature.min(), X_feature.max(), 233).reshape(-1, 1)
y_pred2 = model2.predict(X_new2)

# 绘制数据点和拟合线
plt1.scatter(X_feature, y, color='blue', label='Actual data')  # 展示实际的数据点
plt1.plot(X_new2, y_pred2, color='red', label='Predicted regression')  # 展示预测的线
plt1.title(f'Relationship Between {selected_feature} and Housing Price ') #标题
plt1.xlabel(selected_feature)
plt1.ylabel('Median house value')
plt1.legend()
plt1.show()
