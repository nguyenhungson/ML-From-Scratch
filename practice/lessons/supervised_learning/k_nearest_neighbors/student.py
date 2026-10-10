"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/k_nearest_neighbors
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class KNN:
    """Hoàn thiện class KNN từ đầu."""
    def __init__(self, k=5):
        """KNN.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: KNN.__init__")

    def _vote(self, neighbor_labels):
        """KNN._vote: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: KNN._vote")

    def predict(self, X_test, X_train, y_train):
        """KNN.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: KNN.predict")
