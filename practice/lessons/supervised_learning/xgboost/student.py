"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/xgboost
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class LogisticLoss:
    """Hoàn thiện class LogisticLoss từ đầu."""
    def __init__(self):
        """LogisticLoss.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LogisticLoss.__init__")

    def loss(self, y, y_pred):
        """LogisticLoss.loss: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LogisticLoss.loss")

    def gradient(self, y, y_pred):
        """LogisticLoss.gradient: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LogisticLoss.gradient")

    def hess(self, y, y_pred):
        """LogisticLoss.hess: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LogisticLoss.hess")


class XGBoost(object):
    """Hoàn thiện class XGBoost từ đầu."""
    def __init__(self, n_estimators=200, learning_rate=0.001, min_samples_split=2, min_impurity=1e-07, max_depth=2):
        """XGBoost.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: XGBoost.__init__")

    def fit(self, X, y):
        """XGBoost.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: XGBoost.fit")

    def predict(self, X):
        """XGBoost.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: XGBoost.predict")
