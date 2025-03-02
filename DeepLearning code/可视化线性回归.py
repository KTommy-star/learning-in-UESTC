# 导入机器学习库
import numpy as np # 处理数据
import matplotlib.pyplot as plt # 可视化
from sklearn.linear_model import LinearRegression # 线性回归模型

# 创建一些模拟数据
np.random.seed(0)  # 设置随机种子以确保结果可复现
X = 2 * np.random.rand(1000, 1)  # 生成1000个0到2之间的随机数
y = 2 + 3 * X + np.random.randn(1000, 1)  # 生成线性关系的数据并添加一些噪声

# 为了可视化，我们也将X和y转换为一维数组
X = X.flatten()
y = y.flatten()

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(X.reshape(-1, 1), y)

# 使用模型进行预测
X_new1 = np.array([0, 2])
y_pred1 = model.predict(X_new1.reshape(-1, 1))

# 绘制数据点和拟合线
plt.scatter(X, y, color='blue')  # 实际的数据点
plt.plot(X_new1, y_pred1, color='red', linewidth=2)  # 预测的线
plt.title('KTommy Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.show()