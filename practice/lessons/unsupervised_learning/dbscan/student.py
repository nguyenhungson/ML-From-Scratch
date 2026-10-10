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
        """DBSCAN.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DBSCAN.__init__")

    def _get_neighbors(self, sample_i):
        """DBSCAN._get_neighbors: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DBSCAN._get_neighbors")

    def _expand_cluster(self, sample_i, neighbors):
        """DBSCAN._expand_cluster: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DBSCAN._expand_cluster")

    def _get_cluster_labels(self):
        """DBSCAN._get_cluster_labels: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DBSCAN._get_cluster_labels")

    def predict(self, X):
        """DBSCAN.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DBSCAN.predict")
