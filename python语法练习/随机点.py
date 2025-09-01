import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def generate_random_points(n):
    # 生成随机数据
    x = np.random.rand(n)
    y = np.random.rand(n)

    # 创建DataFrame
    df = pd.DataFrame({'x': x, 'y': y})

    return df


def plot_points(df):
    # 绘制散点图
    plt.scatter(df['x'], df['y'])
    plt.title('Random Points')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def main():
    # 生成100个随机点
    random_points = generate_random_points(1314)

    # 打印生成的点
    print("生成的随机点：")
    print(random_points)

    # 绘制图像
    plot_points(random_points)


if __name__ == "__main__":
    main()