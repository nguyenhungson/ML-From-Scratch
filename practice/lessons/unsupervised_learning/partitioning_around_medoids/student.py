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
        """PAM.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PAM.__init__")

    def _init_random_medoids(self, X):
        """PAM._init_random_medoids: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PAM._init_random_medoids")

    def _closest_medoid(self, sample, medoids):
        """PAM._closest_medoid: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PAM._closest_medoid")

    def _create_clusters(self, X, medoids):
        """PAM._create_clusters: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PAM._create_clusters")

    def _calculate_cost(self, X, clusters, medoids):
        """PAM._calculate_cost: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PAM._calculate_cost")

    def _get_non_medoids(self, X, medoids):
        """PAM._get_non_medoids: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PAM._get_non_medoids")

    def _get_cluster_labels(self, clusters, X):
        """PAM._get_cluster_labels: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PAM._get_cluster_labels")

    def predict(self, X):
        """PAM.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PAM.predict")
