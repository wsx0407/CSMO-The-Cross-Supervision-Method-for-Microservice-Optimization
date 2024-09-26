#!/usr/bin/python
# -*- coding: UTF-8 -*-


import torch
import torch.nn as nn

# 定义神经网络模型
class NeuralNetwork(nn.Module):
    def __init__(self,dim):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(dim * dim, 100)  # 输入层到隐藏层
        self.fc2 = nn.Linear(100, dim * dim)  # 隐藏层到输出层
        self.dim=dim

    def forward(self, x):
        x = torch.flatten(x, start_dim=1)  # 将输入矩阵展平为一维向量
        x = torch.relu(self.fc1(x))  # 使用 ReLU 激活函数作为隐藏层的激活函数
        x = self.fc2(x)  # 输出层不使用激活函数
        return x.view(-1, self.dim, self.dim)  # 将输出向量重新reshape为36x36的矩阵

