"""BÀI THỰC HÀNH ĐỘC LẬP - unsupervised_learning/dbscan
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class DBSCAN:
    """Hoàn thiện class DBSCAN từ đầu."""
    def __init__(self, eps=1, min_samples=5):
        pass

    def _get_neighbors(self, sample_i):
        pass

    def _expand_cluster(self, sample_i, neighbors):
        pass

    def _get_cluster_labels(self):
        pass

    def predict(self, X):
        pass
