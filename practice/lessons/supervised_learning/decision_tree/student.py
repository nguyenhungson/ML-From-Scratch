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
        """DecisionNode.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DecisionNode.__init__")


class DecisionTree(object):
    """Hoàn thiện class DecisionTree từ đầu."""
    def __init__(self, min_samples_split=2, min_impurity=1e-07, max_depth=float('inf'), loss=None):
        """DecisionTree.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DecisionTree.__init__")

    def fit(self, X, y, loss=None):
        """DecisionTree.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DecisionTree.fit")

    def _build_tree(self, X, y, current_depth=0):
        """DecisionTree._build_tree: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DecisionTree._build_tree")

    def predict_value(self, x, tree=None):
        """DecisionTree.predict_value: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DecisionTree.predict_value")

    def predict(self, X):
        """DecisionTree.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DecisionTree.predict")

    def print_tree(self, tree=None, indent=' '):
        """DecisionTree.print_tree: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DecisionTree.print_tree")


class XGBoostRegressionTree(DecisionTree):
    """Hoàn thiện class XGBoostRegressionTree từ đầu."""
    def _split(self, y):
        """XGBoostRegressionTree._split: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: XGBoostRegressionTree._split")

    def _gain(self, y, y_pred):
        """XGBoostRegressionTree._gain: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: XGBoostRegressionTree._gain")

    def _gain_by_taylor(self, y, y1, y2):
        """XGBoostRegressionTree._gain_by_taylor: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: XGBoostRegressionTree._gain_by_taylor")

    def _approximate_update(self, y):
        """XGBoostRegressionTree._approximate_update: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: XGBoostRegressionTree._approximate_update")

    def fit(self, X, y):
        """XGBoostRegressionTree.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: XGBoostRegressionTree.fit")


class RegressionTree(DecisionTree):
    """Hoàn thiện class RegressionTree từ đầu."""
    def _calculate_variance_reduction(self, y, y1, y2):
        """RegressionTree._calculate_variance_reduction: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RegressionTree._calculate_variance_reduction")

    def _mean_of_y(self, y):
        """RegressionTree._mean_of_y: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RegressionTree._mean_of_y")

    def fit(self, X, y):
        """RegressionTree.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RegressionTree.fit")


class ClassificationTree(DecisionTree):
    """Hoàn thiện class ClassificationTree từ đầu."""
    def _calculate_information_gain(self, y, y1, y2):
        """ClassificationTree._calculate_information_gain: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ClassificationTree._calculate_information_gain")

    def _majority_vote(self, y):
        """ClassificationTree._majority_vote: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ClassificationTree._majority_vote")

    def fit(self, X, y):
        """ClassificationTree.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ClassificationTree.fit")
