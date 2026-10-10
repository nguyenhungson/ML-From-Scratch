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
        """NeuralNetwork.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NeuralNetwork.__init__")

    def set_trainable(self, trainable):
        """NeuralNetwork.set_trainable: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NeuralNetwork.set_trainable")

    def add(self, layer):
        """NeuralNetwork.add: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NeuralNetwork.add")

    def test_on_batch(self, X, y):
        """NeuralNetwork.test_on_batch: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NeuralNetwork.test_on_batch")

    def train_on_batch(self, X, y):
        """NeuralNetwork.train_on_batch: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NeuralNetwork.train_on_batch")

    def fit(self, X, y, n_epochs, batch_size):
        """NeuralNetwork.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NeuralNetwork.fit")

    def _forward_pass(self, X, training=True):
        """NeuralNetwork._forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NeuralNetwork._forward_pass")

    def _backward_pass(self, loss_grad):
        """NeuralNetwork._backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NeuralNetwork._backward_pass")

    def summary(self, name='Model Summary'):
        """NeuralNetwork.summary: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NeuralNetwork.summary")

    def predict(self, X):
        """NeuralNetwork.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NeuralNetwork.predict")
