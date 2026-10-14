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
        self.y = y
        self.classes = np.unique(y)
        self.means, self.vars = [], []

        for c in self.classes:
            X_c = X[y == c]
            mean = np.mean(X_c, axis=0)
            var = np.var(X_c, axis=0)

            self.means.append(mean)
            self.vars.append(var)

        self.means = np.array(self.means)
        self.vars = np.array(self.vars)

    def _calculate_likelihood(self, mean, var, x):
        likelihood = 1 / np.sqrt(2 * np.pi * var) * np.exp(-np.square(x - mean) / (2 * var))
        return likelihood
    
    def _calculate_prior(self, c):
        return np.sum(self.y == c) / len(self.y)
        pass

    def _classify(self, sample):
        scores = []
        for i, c in enumerate(self.classes):
            prior = self._calculate_prior(c)
            likelihood = self._calculate_likelihood(self.means[i], self.vars[i], sample)
            log_score = np.log(prior) + np.sum(np.log(likelihood))
            scores.append(log_score)
        return self.classes[np.argmax(scores)]
        pass

    def predict(self, X):
        predictions = []
        for sample in X:
            predictions.append(self._classify(sample))
        return np.array(predictions)
        pass
