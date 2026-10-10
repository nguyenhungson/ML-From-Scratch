"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/regression
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class l1_regularization:
    """Hoàn thiện class l1_regularization từ đầu."""
    def __init__(self, alpha):
        """l1_regularization.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: l1_regularization.__init__")

    def __call__(self, w):
        """l1_regularization.__call__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: l1_regularization.__call__")

    def grad(self, w):
        """l1_regularization.grad: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: l1_regularization.grad")


class l2_regularization:
    """Hoàn thiện class l2_regularization từ đầu."""
    def __init__(self, alpha):
        """l2_regularization.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: l2_regularization.__init__")

    def __call__(self, w):
        """l2_regularization.__call__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: l2_regularization.__call__")

    def grad(self, w):
        """l2_regularization.grad: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: l2_regularization.grad")


class l1_l2_regularization:
    """Hoàn thiện class l1_l2_regularization từ đầu."""
    def __init__(self, alpha, l1_ratio=0.5):
        """l1_l2_regularization.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: l1_l2_regularization.__init__")

    def __call__(self, w):
        """l1_l2_regularization.__call__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: l1_l2_regularization.__call__")

    def grad(self, w):
        """l1_l2_regularization.grad: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: l1_l2_regularization.grad")


class Regression(object):
    """Hoàn thiện class Regression từ đầu."""
    def __init__(self, n_iterations, learning_rate):
        """Regression.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Regression.__init__")

    def initialize_weights(self, n_features):
        """Regression.initialize_weights: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Regression.initialize_weights")

    def fit(self, X, y):
        """Regression.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Regression.fit")

    def predict(self, X):
        """Regression.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Regression.predict")


class LinearRegression(Regression):
    """Hoàn thiện class LinearRegression từ đầu."""
    def __init__(self, n_iterations=100, learning_rate=0.001, gradient_descent=True):
        """LinearRegression.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LinearRegression.__init__")

    def fit(self, X, y):
        """LinearRegression.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LinearRegression.fit")


class LassoRegression(Regression):
    """Hoàn thiện class LassoRegression từ đầu."""
    def __init__(self, degree, reg_factor, n_iterations=3000, learning_rate=0.01):
        """LassoRegression.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LassoRegression.__init__")

    def fit(self, X, y):
        """LassoRegression.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LassoRegression.fit")

    def predict(self, X):
        """LassoRegression.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LassoRegression.predict")


class PolynomialRegression(Regression):
    """Hoàn thiện class PolynomialRegression từ đầu."""
    def __init__(self, degree, n_iterations=3000, learning_rate=0.001):
        """PolynomialRegression.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PolynomialRegression.__init__")

    def fit(self, X, y):
        """PolynomialRegression.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PolynomialRegression.fit")

    def predict(self, X):
        """PolynomialRegression.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PolynomialRegression.predict")


class RidgeRegression(Regression):
    """Hoàn thiện class RidgeRegression từ đầu."""
    def __init__(self, reg_factor, n_iterations=1000, learning_rate=0.001):
        """RidgeRegression.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RidgeRegression.__init__")


class PolynomialRidgeRegression(Regression):
    """Hoàn thiện class PolynomialRidgeRegression từ đầu."""
    def __init__(self, degree, reg_factor, n_iterations=3000, learning_rate=0.01, gradient_descent=True):
        """PolynomialRidgeRegression.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PolynomialRidgeRegression.__init__")

    def fit(self, X, y):
        """PolynomialRidgeRegression.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PolynomialRidgeRegression.fit")

    def predict(self, X):
        """PolynomialRidgeRegression.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PolynomialRidgeRegression.predict")


class ElasticNet(Regression):
    """Hoàn thiện class ElasticNet từ đầu."""
    def __init__(self, degree=1, reg_factor=0.05, l1_ratio=0.5, n_iterations=3000, learning_rate=0.01):
        """ElasticNet.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ElasticNet.__init__")

    def fit(self, X, y):
        """ElasticNet.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ElasticNet.fit")

    def predict(self, X):
        """ElasticNet.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ElasticNet.predict")
