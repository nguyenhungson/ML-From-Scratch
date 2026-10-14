"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/k_nearest_neighbors
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class KNN:
    """Hoàn thiện class KNN từ đầu."""
    def __init__(self, k=5):
        self.k = k
        pass

    def euclidian_dist(self, z1, z2):
        return np.sqrt(np.sum(np.square(z1 - z2)))

    def _vote(self, neighbor_labels):
        values, counts = np.unique(neighbor_labels, return_counts=True)
        return values[np.argmax(counts)]
        pass

    def predict(self, X_test, X_train, y_train):
        predictions = []
        for x in X_test:
            dists = []
            for x_train in X_train:
                dist = self.euclidian_dist(x, x_train)
                dists.append(dist)
            ind = np.argsort(dists)[:self.k]
            neighbor_labels = y_train[ind]
            prediction = self._vote(neighbor_labels)
            predictions.append(prediction)
        return np.array(predictions)    
        pass
