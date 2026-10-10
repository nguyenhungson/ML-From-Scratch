"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/random_forest
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class RandomForest:
    """Hoàn thiện class RandomForest từ đầu."""
    def __init__(self, n_estimators=100, max_features=None, min_samples_split=2, min_gain=0, max_depth=float('inf')):
        """RandomForest.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RandomForest.__init__")

    def fit(self, X, y):
        """RandomForest.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RandomForest.fit")

    def predict(self, X):
        """RandomForest.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RandomForest.predict")
