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
        """KMeans.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: KMeans.__init__")

    def _init_random_centroids(self, X):
        """KMeans._init_random_centroids: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: KMeans._init_random_centroids")

    def _closest_centroid(self, sample, centroids):
        """KMeans._closest_centroid: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: KMeans._closest_centroid")

    def _create_clusters(self, centroids, X):
        """KMeans._create_clusters: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: KMeans._create_clusters")

    def _calculate_centroids(self, clusters, X):
        """KMeans._calculate_centroids: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: KMeans._calculate_centroids")

    def _get_cluster_labels(self, clusters, X):
        """KMeans._get_cluster_labels: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: KMeans._get_cluster_labels")

    def predict(self, X):
        """KMeans.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: KMeans.predict")
