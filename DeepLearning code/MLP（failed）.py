import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torch import optim
from d2l import torch as d2l

# 初始化模型参数
num_inputs, num_outputs, num_hiddens = 784, 10, 256

# 定义模型类
class MLP(nn.Module):
    def __init__(self, num_inputs, num_hiddens, num_outputs):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(num_inputs, num_hiddens)
        self.fc2 = nn.Linear(num_hiddens, num_outputs)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = x.view(-1, num_inputs)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

net = MLP(num_inputs, num_hiddens, num_outputs)

# 损失函数
loss = nn.CrossEntropyLoss()

# 数据加载器
batch_size = 256
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

try:
    # 尝试下载训练集
    train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    # 尝试下载测试集
    test_data = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
except Exception as e:
    print(f"下载数据集时出现错误: {e}")
    print("请手动下载数据集并放置在指定目录，或检查网络连接。")
else:
    train_iter = DataLoader(train_data, batch_size=batch_size, shuffle=True)
    test_iter = DataLoader(test_data, batch_size=batch_size, shuffle=False)

    # 训练参数
    num_epochs, lr = 10, 0.1
    updater = optim.SGD(net.parameters(), lr=lr)

    # 修正参数顺序调用 train_ch13 函数
    d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, updater)

    # 进行预测
    d2l.predict_ch3(net, test_iter)
