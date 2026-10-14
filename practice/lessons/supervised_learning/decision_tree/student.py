"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/decision_tree
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class DecisionNode:
    """Hoàn thiện class DecisionNode từ đầu."""
    def __init__(self, feature_i=None, threshold=None, value=None, true_branch=None, false_branch=None):
        pass


class DecisionTree(object):
    """Hoàn thiện class DecisionTree từ đầu."""
    def __init__(self, min_samples_split=2, min_impurity=1e-07, max_depth=float('inf'), loss=None):
        pass

    def fit(self, X, y, loss=None):
        pass

    def _build_tree(self, X, y, current_depth=0):
        pass

    def predict_value(self, x, tree=None):
        pass

    def predict(self, X):
        pass

    def print_tree(self, tree=None, indent=' '):
        pass


class XGBoostRegressionTree(DecisionTree):
    """Hoàn thiện class XGBoostRegressionTree từ đầu."""
    def _split(self, y):
        pass

    def _gain(self, y, y_pred):
        pass

    def _gain_by_taylor(self, y, y1, y2):
        pass

    def _approximate_update(self, y):
        pass

    def fit(self, X, y):
        pass


class RegressionTree(DecisionTree):
    """Hoàn thiện class RegressionTree từ đầu."""
    def _calculate_variance_reduction(self, y, y1, y2):
        pass

    def _mean_of_y(self, y):
        pass

    def fit(self, X, y):
        pass


class ClassificationTree(DecisionTree):
    """Hoàn thiện class ClassificationTree từ đầu."""
    def _calculate_information_gain(self, y, y1, y2):
        pass

    def _majority_vote(self, y):
        pass

    def fit(self, X, y):
        pass
