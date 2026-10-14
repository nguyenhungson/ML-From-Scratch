"""BÀI THỰC HÀNH ĐỘC LẬP - unsupervised_learning/autoencoder
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class Autoencoder:
    """Hoàn thiện class Autoencoder từ đầu."""
    def __init__(self):
        pass

    def build_encoder(self, optimizer, loss_function):
        pass

    def build_decoder(self, optimizer, loss_function):
        pass

    def train(self, n_epochs, batch_size=128, save_interval=50):
        pass

    def save_imgs(self, epoch, X):
        pass
