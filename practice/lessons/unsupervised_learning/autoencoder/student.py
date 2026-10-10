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
        """Autoencoder.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Autoencoder.__init__")

    def build_encoder(self, optimizer, loss_function):
        """Autoencoder.build_encoder: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Autoencoder.build_encoder")

    def build_decoder(self, optimizer, loss_function):
        """Autoencoder.build_decoder: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Autoencoder.build_decoder")

    def train(self, n_epochs, batch_size=128, save_interval=50):
        """Autoencoder.train: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Autoencoder.train")

    def save_imgs(self, epoch, X):
        """Autoencoder.save_imgs: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Autoencoder.save_imgs")
