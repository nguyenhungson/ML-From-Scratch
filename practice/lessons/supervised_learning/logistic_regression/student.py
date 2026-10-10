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
        """LogisticRegression.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LogisticRegression.__init__")

    def _initialize_parameters(self, X):
        """LogisticRegression._initialize_parameters: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LogisticRegression._initialize_parameters")

    def fit(self, X, y, n_iterations=4000):
        """LogisticRegression.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LogisticRegression.fit")

    def predict(self, X):
        """LogisticRegression.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LogisticRegression.predict")
