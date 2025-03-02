import torch
import torch.nn as nn
import torch.nn.functional as F


# 定义缩放点积注意力类
class ScaledDotProductAttention(nn.Module):
    def __init__(self, embed_size):
        super(ScaledDotProductAttention, self).__init__()
        # 初始化缩放因子为嵌入维度的平方根
        self.scale = torch.sqrt(torch.FloatTensor([embed_size]))

    def forward(self, q, k, v):
        # 确保scale在相同的设备上
        self.scale = self.scale.to(q.device)
        # 计算查询和键的点积，并进行转置操作以匹配维度
        attention_scores = torch.matmul(q, k.transpose(-2, -1))
        # 缩放点积
        attention_scores = attention_scores / self.scale
        # 应用softmax获取注意力权重
        attention_weights = F.softmax(attention_scores, dim=-1)
        # 计算加权的值
        output = torch.matmul(attention_weights, v)
        return output, attention_weights


# 定义前馈网络类
class PositionwiseFeedforward(nn.Module):
    def __init__(self, embed_size, forward_expansion):
        super(PositionwiseFeedforward, self).__init__()
        # 第一个线性层
        self.fc1 = nn.Linear(embed_size, forward_expansion * embed_size)
        # 第二个线性层
        self.fc2 = nn.Linear(forward_expansion * embed_size, embed_size)

    def forward(self, x):
        # 通过前馈网络
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# 定义Transformer块类
class TransformerBlock(nn.Module):
    def __init__(self, embed_size, forward_expansion):
        super(TransformerBlock, self).__init__()
        # 初始化缩放点积注意力
        self.attention = ScaledDotProductAttention(embed_size)
        # 第一个层归一化
        self.norm1 = nn.LayerNorm(embed_size)
        # 第二个层归一化
        self.norm2 = nn.LayerNorm(embed_size)
        # 初始化前馈网络
        self.feedforward = PositionwiseFeedforward(embed_size, forward_expansion)

    def forward(self, value, key, query, mask=None):
        # 自注意力层
        attention, weights = self.attention(query, key, value)
        # 残差连接和层归一化
        x = self.norm1(attention + query)
        # 前馈网络
        forward = self.feedforward(x)
        # 第二个残差连接和层归一化
        out = self.norm2(forward + x)
        return out, weights


# 定义简化的Transformer模型类
class SimpleTransformer(nn.Module):
    def __init__(self, embed_size, src_vocab_size, trg_vocab_size, forward_expansion):
        super(SimpleTransformer, self).__init__()
        # 源语言词嵌入层
        self.src_embedding = nn.Embedding(src_vocab_size, embed_size)
        # 目标语言词嵌入层
        self.trg_embedding = nn.Embedding(trg_vocab_size, embed_size)
        # 位置编码
        self.positional_encoding = nn.Parameter(torch.zeros(1, max(src_vocab_size, trg_vocab_size), embed_size))
        # Transformer块
        self.transformer_block = TransformerBlock(embed_size, forward_expansion)
        # 输出层
        self.fc_out = nn.Linear(embed_size, trg_vocab_size)

    def forward(self, src, trg):
        # 词嵌入和位置编码
        src_embedding = self.src_embedding(src) + self.positional_encoding[:, :src.size(1), :]
        trg_embedding = self.trg_embedding(trg) + self.positional_encoding[:, :trg.size(1), :]

        # 创建遮罩，防止关注到pad tokens和未来的tokens
        src_mask = (src != 0).unsqueeze(1).unsqueeze(2)  # (batch_size, 1, 1, src_seq_length)
        trg_mask = (trg != 0).unsqueeze(1).unsqueeze(2)  # (batch_size, 1, 1, trg_seq_length)

        # 通过Transformer块
        output, _ = self.transformer_block(src_embedding, src_embedding, src_embedding, src_mask)
        output, _ = self.transformer_block(trg_embedding, output, trg_embedding, trg_mask)

        # 通过最后的线性层
        output = self.fc_out(output)
        return output


# 示例使用
if __name__ == "__main__":
    # 定义模型参数
    embed_size = 128
    src_vocab_size = 1000
    trg_vocab_size = 1000
    forward_expansion = 4

    # 初始化模型
    model = SimpleTransformer(embed_size, src_vocab_size, trg_vocab_size, forward_expansion)

    # 生成随机的源序列和目标序列
    batch_size = 32
    src_seq_length = 10
    trg_seq_length = 10
    src = torch.randint(0, src_vocab_size, (batch_size, src_seq_length))
    trg = torch.randint(0, trg_vocab_size, (batch_size, trg_seq_length))

    # 前向传播
    output = model(src, trg)

    # 打印输出形状
    print("Output shape:", output.shape)