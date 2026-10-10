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
        """BayesianRegression.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: BayesianRegression.__init__")

    def _draw_scaled_inv_chi_sq(self, n, df, scale):
        """BayesianRegression._draw_scaled_inv_chi_sq: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: BayesianRegression._draw_scaled_inv_chi_sq")

    def fit(self, X, y):
        """BayesianRegression.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: BayesianRegression.fit")

    def predict(self, X, eti=False):
        """BayesianRegression.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: BayesianRegression.predict")
