import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# 创建一个图形
fig, ax = plt.subplots()

# 定义爱心的形状
x = np.linspace(-2, 2, 100)
y = np.sqrt(np.abs(x)) - 0.75 * np.sin(3 * np.pi * x)
ax.plot(x, y, 'r')

# 设置图形范围
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1)

# 隐藏坐标轴
ax.axis('off')

# 创建初始化函数
def init():
    ax.clear()
    return ax,

# 创建更新函数
def update(frame):
    theta = np.radians(frame)
    a = 0.5 * (1 + np.cos(theta))
    # 这里需要重新定义 x 和 y，因为它们依赖于 frame
    x = a * np.sqrt(np.abs(x)) - 0.75 * np.sin(3 * np.pi * x)
    y = a * np.linspace(-2, 2, len(x))
    ax.clear()
    ax.plot(x, y, 'r')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 1)
    return ax,

# 创建动画对象
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 360, 120), init_func=init, blit=True, repeat=True)

# 显示动画
plt.show()