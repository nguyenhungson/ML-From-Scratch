"""BÀI THỰC HÀNH ĐỘC LẬP - unsupervised_learning/generative_adversarial_network
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class GAN:
    """Hoàn thiện class GAN từ đầu."""
    def __init__(self):
        """GAN.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GAN.__init__")

    def build_generator(self, optimizer, loss_function):
        """GAN.build_generator: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GAN.build_generator")

    def build_discriminator(self, optimizer, loss_function):
        """GAN.build_discriminator: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GAN.build_discriminator")

    def train(self, n_epochs, batch_size=128, save_interval=50):
        """GAN.train: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GAN.train")

    def save_imgs(self, epoch):
        """GAN.save_imgs: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GAN.save_imgs")
