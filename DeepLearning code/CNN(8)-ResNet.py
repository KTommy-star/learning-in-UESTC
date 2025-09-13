import torch
from torch import nn
from torch.nn import functional as F
from d2l import torch as d2l


class Residual(nn.Module):  #@save
    def __init__(self, input_channels, num_channels,
                 use_1x1conv=False, strides=1):
        super().__init__()
        self.conv1 = nn.Conv2d(input_channels, num_channels,
                               kernel_size=3, padding=1, stride=strides)
        self.conv2 = nn.Conv2d(num_channels, num_channels,
                               kernel_size=3, padding=1)
        if use_1x1conv:#当use_1x1conv=True时，添加通过1*1卷积调整通道和分辨率，使输入与输出形状匹配；否则不添加该卷积。
            self.conv3 = nn.Conv2d(input_channels, num_channels,
                                   kernel_size=1, stride=strides)
        else:#当use_1x1conv=False时，应用ReLU非线性函数之前，将输入添加到输出。
            self.conv3 = None
        self.bn1 = nn.BatchNorm2d(num_channels)
        self.bn2 = nn.BatchNorm2d(num_channels)
        self.relu=nn.ReLU(inplace=True)#启用原地操作，即直接修改输入张量的数据，而不是创建新的输出张量，可以省内存，提速
    def forward(self, X):
        Y = F.relu(self.bn1(self.conv1(X)))
        Y = self.bn2(self.conv2(Y))
        if self.conv3:
            X = self.conv3(X)
        Y += X
        return F.relu(Y)
#查看输入和输出形状一致的情况
blk = Residual(3,3)
X = torch.rand(4, 3, 6, 6)
Y = blk(X)
print(Y.shape)
#在增加输出通道数的同时，减半输出的高和宽
blk = Residual(3,6, use_1x1conv=True, strides=2)
print(blk(X).shape)
#ResNet的前两层跟之前介绍的GoogLeNet中的一样： 在输出通道数为64、步幅为2的卷积层后，接步幅为2的的最大汇聚层。
b1 = nn.Sequential(nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3),
                   nn.BatchNorm2d(64), nn.ReLU(),#不同之处在于ResNet每个卷积层后增加了批量规范化层。
                   nn.MaxPool2d(kernel_size=3, stride=2, padding=1))
#现在定义残差块：
def resnet_block(input_channels, num_channels, num_residuals,
                 first_block=False):
    blk = []
    for i in range(num_residuals):
        if i == 0 and not first_block:#当前阶段不是第一个残差块阶段（first_block=False）时，该阶段的第一个残差块（i=0）需要高宽减半（即下采样）
            blk.append(Residual(input_channels, num_channels,
                                use_1x1conv=True, strides=2))
        else:#first_block=true，现在是第一个残差块阶段，通常已通过一个步幅为2的卷积或池化层，无续再调整高宽
            blk.append(Residual(num_channels, num_channels))
    return blk
'''回答问题：为什么需要高宽减半？
1.逐步降低分辨率（高宽减半）；特征图尺寸减半，计算量减少
2.扩大视野（感受野）；随着分辨率降低，每个像素对应原始图像的区域更大，能捕捉更大范围的模式。
3.理解全局特征（如物体形状、位置关系）；通常在高宽减半时，通道数加倍（如从 64 通道变为 128 通道），保留更多抽象特征'''
#接着在ResNet加入所有残差块，这里每个模块使用2个残差块
b2 = nn.Sequential(*resnet_block(64, 64, 2, first_block=True))
b3 = nn.Sequential(*resnet_block(64, 128, 2))
b4 = nn.Sequential(*resnet_block(128, 256, 2))
b5 = nn.Sequential(*resnet_block(256, 512, 2))
#最后，加入全局平均池化层，以及全连接层输出
net = nn.Sequential(b1, b2, b3, b4, b5,
                    nn.AdaptiveAvgPool2d((1,1)),
                    nn.Flatten(), nn.Linear(512, 10))
#观察一下ResNet中不同模块的输入形状是如何变化的
X = torch.rand(size=(1, 1, 224, 224))
for layer in net:
    X = layer(X)
    print(layer.__class__.__name__,'output shape:\t', X.shape)
#设置超参数，开始训练：
lr, num_epochs, batch_size = 0.05, 10, 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size, resize=96)
d2l.train_ch6(net, train_iter, test_iter, num_epochs, lr, d2l.try_gpu())