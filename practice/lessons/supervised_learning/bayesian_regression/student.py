"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/bayesian_regression
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class BayesianRegression(object):
    """Hoàn thiện class BayesianRegression từ đầu."""
    def __init__(self, n_draws, mu0, omega0, nu0, sigma_sq0, poly_degree=0, cred_int=95):
        pass

    def _draw_scaled_inv_chi_sq(self, n, df, scale):
        pass

    def fit(self, X, y):
        pass

    def predict(self, X, eti=False):
        pass
