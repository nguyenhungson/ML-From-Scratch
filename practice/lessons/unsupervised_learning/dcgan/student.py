"""BÀI THỰC HÀNH ĐỘC LẬP - unsupervised_learning/dcgan
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class DCGAN:
    """Hoàn thiện class DCGAN từ đầu."""
    def __init__(self):
        """DCGAN.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DCGAN.__init__")

    def build_generator(self, optimizer, loss_function):
        """DCGAN.build_generator: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DCGAN.build_generator")

    def build_discriminator(self, optimizer, loss_function):
        """DCGAN.build_discriminator: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DCGAN.build_discriminator")

    def train(self, epochs, batch_size=128, save_interval=50):
        """DCGAN.train: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DCGAN.train")

    def save_imgs(self, epoch):
        """DCGAN.save_imgs: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DCGAN.save_imgs")
