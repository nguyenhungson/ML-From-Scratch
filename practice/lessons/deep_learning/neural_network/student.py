"""BÀI THỰC HÀNH ĐỘC LẬP - deep_learning/neural_network
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class NeuralNetwork:
    """Hoàn thiện class NeuralNetwork từ đầu."""
    def __init__(self, optimizer, loss, validation_data=None):
        pass

    def set_trainable(self, trainable):
        pass

    def add(self, layer):
        pass

    def test_on_batch(self, X, y):
        pass

    def train_on_batch(self, X, y):
        pass

    def fit(self, X, y, n_epochs, batch_size):
        pass

    def _forward_pass(self, X, training=True):
        pass

    def _backward_pass(self, loss_grad):
        pass

    def summary(self, name='Model Summary'):
        pass

    def predict(self, X):
        pass
