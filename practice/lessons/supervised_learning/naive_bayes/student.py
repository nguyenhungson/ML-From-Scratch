"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/naive_bayes
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class NaiveBayes:
    """Hoàn thiện class NaiveBayes từ đầu."""
    def fit(self, X, y):
        """NaiveBayes.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NaiveBayes.fit")

    def _calculate_likelihood(self, mean, var, x):
        """NaiveBayes._calculate_likelihood: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NaiveBayes._calculate_likelihood")

    def _calculate_prior(self, c):
        """NaiveBayes._calculate_prior: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NaiveBayes._calculate_prior")

    def _classify(self, sample):
        """NaiveBayes._classify: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NaiveBayes._classify")

    def predict(self, X):
        """NaiveBayes.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NaiveBayes.predict")
