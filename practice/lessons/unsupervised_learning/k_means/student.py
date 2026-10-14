"""BÀI THỰC HÀNH ĐỘC LẬP - unsupervised_learning/k_means
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class KMeans:
    """Hoàn thiện class KMeans từ đầu."""
    def __init__(self, k=2, max_iterations=500):
        pass

    def _init_random_centroids(self, X):
        pass

    def _closest_centroid(self, sample, centroids):
        pass

    def _create_clusters(self, centroids, X):
        pass

    def _calculate_centroids(self, clusters, X):
        pass

    def _get_cluster_labels(self, clusters, X):
        pass

    def predict(self, X):
        pass
