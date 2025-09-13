#自定义块，这里以MLP为例：
import torch
from torch import nn
from torch.nn import functional as F
#nn.Sequential定义了一个特殊的Module，维护了一个由Module组成的有序列表
net = nn.Sequential(nn.Linear(20, 256), nn.ReLU(), nn.Linear(256, 10))

X = torch.rand(2, 20)
net(X)
'''以上是定义了一个简单的网络'''
class MLP(nn.Module):
    # 用模型参数声明层。这里，我们声明两个全连接的层
    def __init__(self):
        # 调用MLP的父类Module的构造函数来执行必要的初始化。
        # 这样，在类实例化时也可以指定其他函数参数，例如模型参数params（稍后将介绍）
        super().__init__()
        self.hidden = nn.Linear(20, 256)  # 隐藏层
        self.out = nn.Linear(256, 10)  # 输出层

    # 定义模型的前向传播，即如何根据输入X返回所需的模型输出
    def forward(self, X):
        # 注意，这里我们使用ReLU的函数版本，其在nn.functional模块中定义。
        return self.out(F.relu(self.hidden(X)))
#MySequential:功能类似于Sequential
class MySequential(nn.Module):
    def __init__(self, *args):
        super().__init__()
        for idx, module in enumerate(args):
            # 这里，module是Module子类的一个实例。我们把它保存在'Module'类的成员
            # 变量_modules中。_module的类型是OrderedDict
            self._modules[str(idx)] = module

    def forward(self, X):
        # OrderedDict保证了按照成员添加的顺序遍历它们
        for block in self._modules.values():
            X = block(X)
        return X
#二维卷积：通过卷积核（矩阵）对图片进行“扫描”获取相应的属性
import torch
from torch import nn
from d2l import torch as d2l
#二维内积运算的函数
def corr2d(X, K):  #@save
    """计算二维互相关运算"""
    h, w = K.shape#行数、列数；K是卷积核
    Y = torch.zeros((X.shape[0] - h + 1, X.shape[1] - w + 1))#构建输出矩阵，这里明确了矩阵的规格，这个数学公式，很重要！！！
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            Y[i, j] = (X[i:i + h, j:j + w] * K).sum()
    return Y
#举例示范
X = torch.tensor([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]])
K = torch.tensor([[0.0, 1.0], [2.0, 3.0]])
print(corr2d(X, K))
#实现二维卷积层
class Conv2D(nn.Module):
    def __init__(self,kernel_size):
        super().__init__()
        self.weight=nn.Parameter(torch.rand(kernel_size))
        self.bias=nn.Parameter(torch.zeros(1))
    def forward(self,x):
        return corr2d(x,self.weight) + self.bias
#卷积层的一个简单应用：图像中目标的边缘检测：
X = torch.ones((6, 8))
X[:, 2:6] = 0
K = torch.tensor([[1.0, -1.0]])
Y = corr2d(X, K)
Y = corr2d(X, K)#将输入的二维图像转置，再进行如上的互相关运算。 之前检测到的垂直边缘消失了。
# 不出所料，这个卷积核K只可以检测垂直边缘，无法检测水平边缘。
#学习卷积核：通过仅查看“输入-输出”对来学习由X生成Y的卷积核

# 构造一个二维卷积层，它具有1个输出通道和形状为（1，2）的卷积核
conv2d = nn.Conv2d(1,1, kernel_size=(1, 2), bias=False)

# 这个二维卷积层使用四维输入和输出格式（批量大小、通道、高度、宽度），
# 其中批量大小和通道数都为1
X = X.reshape((1, 1, 6, 8))
Y = Y.reshape((1, 1, 6, 7))
lr = 3e-2  # 学习率

for i in range(10):
    Y_hat = conv2d(X)
    l = (Y_hat - Y) ** 2
    conv2d.zero_grad()
    l.sum().backward()
    # 迭代卷积核
    conv2d.weight.data[:] -= lr * conv2d.weight.grad
    if (i + 1) % 2 == 0:
        print(f'epoch {i+1}, loss {l.sum():.3f}')
conv2d.weight.data.reshape((1, 2))#看看我们所学的卷积核的权重张量