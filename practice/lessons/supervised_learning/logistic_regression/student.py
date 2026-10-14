"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/logistic_regression
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class LogisticRegression:
    """Hoàn thiện class LogisticRegression từ đầu."""
    def __init__(self, learning_rate=0.1, gradient_descent=True):
        self.learning_rate = learning_rate
        self.gradient_descent = gradient_descent
        pass

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def _initialize_parameters(self, X):
        self.w = np.random.randn(X.shape[1])
        self.b = 0.0
        pass

    def fit(self, X, y, n_iterations=4000):
        losses = []
        self._initialize_parameters(X)
        m = X.shape[0]
        for _ in range(n_iterations):
            z = X @ self.w + self.b
            y_pred = self.sigmoid(z)
            error = y_pred - y
            loss = - np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
            losses.append(loss)
            dw = (1/m) * (X.T @ error)
            db = (1/m) * np.sum(error)
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db
        return losses
        pass

    def predict(self, X):
        val = self.sigmoid(X @ self.w + self.b)
        return np.where(val >= 0.5, 1, 0)
        pass
