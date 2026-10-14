"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/gradient_boosting
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class GradientBoosting(object):
    """Hoàn thiện class GradientBoosting từ đầu."""
    def __init__(self, n_estimators, learning_rate, min_samples_split, min_impurity, max_depth, regression):
        pass

    def fit(self, X, y):
        pass

    def predict(self, X):
        pass


class GradientBoostingRegressor(GradientBoosting):
    """Hoàn thiện class GradientBoostingRegressor từ đầu."""
    def __init__(self, n_estimators=200, learning_rate=0.5, min_samples_split=2, min_var_red=1e-07, max_depth=4, debug=False):
        pass


class GradientBoostingClassifier(GradientBoosting):
    """Hoàn thiện class GradientBoostingClassifier từ đầu."""
    def __init__(self, n_estimators=200, learning_rate=0.5, min_samples_split=2, min_info_gain=1e-07, max_depth=2, debug=False):
        pass

    def fit(self, X, y):
        pass
