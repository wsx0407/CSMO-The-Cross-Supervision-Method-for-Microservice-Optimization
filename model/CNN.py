import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.backends.cudnn as cudnn
from torch.utils.tensorboard import SummaryWriter

class Encoder(nn.Module):
    def __init__(self):
        super(Encoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 16, 3, stride=1, padding=1),  # output: 16 x dim x dim
            nn.ReLU(),
            nn.Conv2d(16, 32, 3, stride=2, padding=1),  # output: 32 x dim/2 x dim/2
            nn.ReLU(),
            nn.Conv2d(32, 64, 3, stride=2, padding=1),  # output: 64 x dim/4 x dim/4
            nn.ReLU(),
            nn.ConvTranspose2d(64, 128, 4, stride=2, padding=1),  # output: 128 x dim/2 x dim/2
            nn.ReLU(),
            nn.ConvTranspose2d(128, 64, 6, stride=2, padding=1),  # output: 64 x dim x dim
            nn.ReLU(),
            nn.ConvTranspose2d(64, 3, 6, stride=1, padding=2),  # output: 3 x 64 x 64
        )

    def forward(self, x):
        return self.encoder(x)

class Decoder(nn.Module):
    def __init__(self, dim):
        super(Decoder, self).__init__()
        self.decoder = nn.Sequential(
            nn.Conv2d(3, 64, 3, stride=1, padding=1),  # output: 64 x 64 x 64
            nn.ReLU(),
            nn.Conv2d(64, 64, 3, stride=1, padding=1),  # output: 64 x 64 x 64
            nn.ReLU(),
            nn.ConvTranspose2d(64, 32, 4, stride=2, padding=1),  # output: 32 x 32 x 32
            nn.ReLU(),
            nn.Conv2d(32, 16, 3, stride=1, padding=1),  # output: 16 x 32 x 32
            nn.ReLU(),
            nn.Conv2d(16, 1, 3, stride=1, padding=1),  # output: 1 x 32 x 32
            nn.AdaptiveAvgPool2d((dim, dim))  # output: 1 x dim x dim
        )

    def forward(self, x):
        return self.decoder(x)

class AE(nn.Module):
    def __init__(self, dim):
        super(AE, self).__init__()
        self.encoder = Encoder()
        self.decoder = Decoder(dim)

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded