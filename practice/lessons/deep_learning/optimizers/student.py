"""BÀI THỰC HÀNH ĐỘC LẬP - deep_learning/optimizers
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class StochasticGradientDescent:
    """Hoàn thiện class StochasticGradientDescent từ đầu."""
    def __init__(self, learning_rate=0.01, momentum=0):
        pass

    def update(self, w, grad_wrt_w):
        pass


class NesterovAcceleratedGradient:
    """Hoàn thiện class NesterovAcceleratedGradient từ đầu."""
    def __init__(self, learning_rate=0.001, momentum=0.4):
        pass

    def update(self, w, grad_func):
        pass


class Adagrad:
    """Hoàn thiện class Adagrad từ đầu."""
    def __init__(self, learning_rate=0.01):
        pass

    def update(self, w, grad_wrt_w):
        pass


class Adadelta:
    """Hoàn thiện class Adadelta từ đầu."""
    def __init__(self, rho=0.95, eps=1e-06):
        pass

    def update(self, w, grad_wrt_w):
        pass


class RMSprop:
    """Hoàn thiện class RMSprop từ đầu."""
    def __init__(self, learning_rate=0.01, rho=0.9):
        pass

    def update(self, w, grad_wrt_w):
        pass


class Adam:
    """Hoàn thiện class Adam từ đầu."""
    def __init__(self, learning_rate=0.001, b1=0.9, b2=0.999):
        pass

    def update(self, w, grad_wrt_w):
        pass
