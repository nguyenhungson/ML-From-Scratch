"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/perceptron
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class Perceptron:
    """Hoàn thiện class Perceptron từ đầu."""
    def __init__(self, n_iterations=20000, activation_function=None, loss=None, learning_rate=0.01):
        """Perceptron.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Perceptron.__init__")

    def fit(self, X, y):
        """Perceptron.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Perceptron.fit")

    def predict(self, X):
        """Perceptron.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Perceptron.predict")
