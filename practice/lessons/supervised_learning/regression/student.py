
"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/regression
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method.
"""
from __future__ import annotations

import math
import numpy as np


class l1_regularization:
    """Hoàn thiện class l1_regularization từ đầu."""

    def __init__(self, alpha):
        self.alpha = alpha

    def __call__(self, w):
        return self.alpha * np.sum(np.abs(w))

    def grad(self, w):
        return self.alpha * np.sign(w)


class l2_regularization:
    """Hoàn thiện class l2_regularization từ đầu."""

    def __init__(self, alpha):
        self.alpha = alpha

    def __call__(self, w):
        return self.alpha * np.sum(np.square(w))
        pass

    def grad(self, w):
        return 2 * self.alpha * w
        pass


class l1_l2_regularization:
    """Hoàn thiện class l1_l2_regularization từ đầu."""

    def __init__(self, alpha, l1_ratio=0.5):
        self.alpha = alpha
        self.l1_ratio = l1_ratio

    def __call__(self, w):
        l1 = self.l1_ratio * np.sum(np.abs(w))
        l2 = (1 - self.l1_ratio) * np.sum(np.square(w))
        return self.alpha * (l1 + l2)

    def grad(self, w):
        l1_grad = self.l1_ratio * np.sign(w)
        l2_grad = 2 * (1 - self.l1_ratio) * w
        return self.alpha * (l1_grad + l2_grad)


class Regression(object):
    """Hoàn thiện class Regression từ đầu."""

    def __init__(self, n_iterations, learning_rate):
        self.n_iterations = n_iterations
        self.learning_rate = learning_rate
        pass

    def initialize_weights(self, n_features):
        self.w = np.random.randn(n_features)
        self.b = 0.0
        pass

    def fit(self, X, y):
        m = X.shape[0]
        self.initialize_weights(X.shape[1])
        for _ in range(self.n_iterations):
            y_pred = X @ self.w + self.b
            error = y_pred - y
            dw = (2 / m) * X.T @ error
            db = (2 / m) * np.sum(error)
            self.w = self.w - dw * self.learning_rate
            self.b = self.b - db * self.learning_rate
        pass

    def predict(self, X):
        return X @ self.w + self.b
        pass


class LinearRegression(Regression):
    """Hoàn thiện class LinearRegression từ đầu."""

    def __init__(
        self,
        n_iterations=100,
        learning_rate=0.001,
        gradient_descent=True
    ):
        super().__init__(n_iterations, learning_rate)
        self.gradient_descent = gradient_descent

    def fit(self, X, y):
        if self.gradient_descent:
            super().fit(X, y)
        else:
            X_aug = np.column_stack([
                np.ones(X.shape[0]),
                X
            ])

            theta = np.linalg.lstsq(
                X_aug, y, rcond=None
            )[0]

            self.b = float(theta[0])
            self.w = theta[1:]

        return self


class LassoRegression(Regression):
    """Hoàn thiện class LassoRegression từ đầu."""

    def __init__(
        self,
        degree,
        reg_factor,
        n_iterations=3000,
        learning_rate=0.01
    ):
        super().__init__(n_iterations, learning_rate)
        self.degree = degree
        self.reg_factor = reg_factor
        self.regularization = l1_regularization(alpha=reg_factor)
        pass

    def fit(self, X, y):
        m = X.shape[0]
        X_poly = []
        for i in range(1, self.degree + 1):
            X_poly.append(X[:, 0] ** i)
        X_poly = np.column_stack(X_poly)
        self.initialize_weights(X_poly.shape[1])
        for _ in range(self.n_iterations):
            y_pred = X_poly @ self.w + self.b
            l1_loss = self.regularization(self.w)
            l1_grad = self.regularization.grad(self.w)
            error = y_pred - y
            loss = np.mean(np.square(error)) + l1_loss
            dw = (2/m) * X_poly.T @ error + l1_grad
            db = (2/m) * np.sum(error)
            self.w = self.w - self.learning_rate * dw
            self.b = self.b - self.learning_rate * db
        pass

    def predict(self, X):
        X_poly = []
        for i in range(1, self.degree + 1):
            X_poly.append(X[:, 0] ** i)
        X_poly = np.column_stack(X_poly)
        y_pred = X_poly @ self.w + self.b
        return y_pred
        pass


class PolynomialRegression(Regression):
    """Hoàn thiện class PolynomialRegression từ đầu."""

    def __init__(
        self,
        degree,
        n_iterations=3000,
        learning_rate=0.001
    ):
        super().__init__(n_iterations, learning_rate)
        self.degree = degree
        pass

    def fit(self, X, y):
        m = X.shape[0]
        X_poly = []
        for i in range(1, self.degree + 1):
            X_poly.append(X[:, 0] ** i)
        X_poly = np.column_stack(X_poly)
        self.initialize_weights(X_poly.shape[1])
        for _ in range(self.n_iterations):
            y_pred = X_poly @ self.w + self.b
            error = y_pred - y
            loss = np.mean(np.square(error))
            dw = (2/m) * (X_poly.T @ error)
            db = (2/m) * np.sum(error)
            self.w = self.w - self.learning_rate * dw
            self.b = self.b - self.learning_rate * db
        pass

    def predict(self, X):
        X_poly = []
        for i in range(1, self.degree + 1):
            X_poly.append(X[:, 0] ** i)
        X_poly = np.column_stack(X_poly)
        y_pred = X_poly @ self.w + self.b
        return y_pred
        pass


class RidgeRegression(Regression):
    """Hoàn thiện class RidgeRegression từ đầu."""

    def __init__(
        self,
        reg_factor,
        n_iterations=1000,
        learning_rate=0.001
    ):
        super().__init__(n_iterations, learning_rate)
        self.reg_factor = reg_factor
        self.regularization = l2_regularization(reg_factor)
        pass
    
    def fit(self, X, y):
        m = X.shape[0]
        self.initialize_weights(X.shape[1])
        self.loss_history = []
        for _ in range(self.n_iterations):
            y_pred = X @ self.w + self.b
            error = y_pred - y
            l2_loss = self.regularization(self.w)
            l2_grad = self.regularization.grad(self.w)
            loss = np.mean(np.square(error)) + l2_loss
            self.loss_history.append(loss)
            dw = (2 / m) * (X.T @ error) + l2_grad
            db = (2 / m) * np.sum(error)
            self.w = self.w - self.learning_rate * dw
            self.b = self.b - self.learning_rate * db
        return self

    def predict(self, X):
        return X @ self.w + self.b

class PolynomialRidgeRegression(Regression):
    """Hoàn thiện class PolynomialRidgeRegression từ đầu."""

    def __init__(
        self,
        degree,
        reg_factor,
        n_iterations=3000,
        learning_rate=0.01,
        gradient_descent=True
    ):
        super().__init__(n_iterations, learning_rate)
        self.degree = degree
        self.reg_factor = reg_factor
        self.gradient_descent = gradient_descent
        self.model = RidgeRegression(self.reg_factor, self.n_iterations, self.learning_rate)
        pass

    def fit(self, X, y):
        X_poly = []

        for i in range(1, self.degree + 1):
            X_poly.append(X[:, 0] ** i)

        X_poly = np.column_stack(X_poly)

        if self.gradient_descent:
            self.model.fit(X_poly, y)

        else:
            m = X_poly.shape[0]

            X_aug = np.column_stack([
                np.ones(m),
                X_poly
            ])

            penalty = np.eye(X_aug.shape[1])
            penalty[0, 0] = 0

            A = (
                X_aug.T @ X_aug
                + m * self.reg_factor * penalty
            )

            theta = np.linalg.pinv(A) @ (X_aug.T @ y)

            self.model.b = float(theta[0])
            self.model.w = theta[1:]

        return self

    def predict(self, X):
        X_poly = []
        for i in range(1, self.degree + 1):
            X_poly.append(X[:, 0] ** i)
        X_poly = np.column_stack(X_poly)
        return self.model.predict(X_poly)
        pass


class ElasticNet(Regression):
    """Hoàn thiện class ElasticNet từ đầu."""

    def __init__(
        self,
        degree=1,
        reg_factor=0.05,
        l1_ratio=0.5,
        n_iterations=3000,
        learning_rate=0.01
    ):
        super().__init__(n_iterations, learning_rate)
        self.degree = degree
        self.reg_factor = reg_factor
        self.l1_ratio = l1_ratio

        self.regularization = l1_l2_regularization(
            alpha=reg_factor,
            l1_ratio=l1_ratio
        )
        pass

    def fit(self, X, y):
        X_poly = []
        for i in range(1, self.degree+1):
            X_poly.append(X[:, 0] ** i)
        X_poly = np.column_stack(X_poly)
        m = X_poly.shape[0]
        self.initialize_weights(X_poly.shape[1])
        for _ in range(self.n_iterations):
            y_pred = X_poly @ self.w + self.b
            l1_l2_loss = self.regularization(self.w)
            l1_l2_grad = self.regularization.grad(self.w)
            error = y_pred - y
            loss = np.mean(np.square(error)) + l1_l2_loss
            dw = (2/m) * (X_poly.T @ error) + l1_l2_grad
            db = (2/m) * np.sum(error)
            self.w = self.w - self.learning_rate * dw
            self.b = self.b - self.learning_rate * db
        
        pass

    def predict(self, X):
        X_poly = []
        for i in range(1, self.degree+1):
            X_poly.append(X[:, 0] ** i)
        X_poly = np.column_stack(X_poly)
        y_pred = X_poly @ self.w + self.b
        return y_pred
        pass
