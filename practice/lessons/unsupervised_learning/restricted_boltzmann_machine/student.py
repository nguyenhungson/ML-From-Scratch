"""BÀI THỰC HÀNH ĐỘC LẬP - unsupervised_learning/restricted_boltzmann_machine
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class RBM:
    """Hoàn thiện class RBM từ đầu."""
    def __init__(self, n_hidden=128, learning_rate=0.1, batch_size=10, n_iterations=100):
        pass

    def _initialize_weights(self, X):
        pass

    def fit(self, X, y=None):
        pass

    def _sample(self, X):
        pass

    def reconstruct(self, X):
        pass
