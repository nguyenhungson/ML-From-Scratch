"""BÀI THỰC HÀNH ĐỘC LẬP - unsupervised_learning/partitioning_around_medoids
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class PAM:
    """Hoàn thiện class PAM từ đầu."""
    def __init__(self, k=2):
        pass

    def _init_random_medoids(self, X):
        pass

    def _closest_medoid(self, sample, medoids):
        pass

    def _create_clusters(self, X, medoids):
        pass

    def _calculate_cost(self, X, clusters, medoids):
        pass

    def _get_non_medoids(self, X, medoids):
        pass

    def _get_cluster_labels(self, clusters, X):
        pass

    def predict(self, X):
        pass
