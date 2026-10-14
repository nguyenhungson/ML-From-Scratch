"""BÀI THỰC HÀNH ĐỘC LẬP - deep_learning/loss_functions
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class Loss(object):
    """Hoàn thiện class Loss từ đầu."""
    def loss(self, y_true, y_pred):
        pass

    def gradient(self, y, y_pred):
        pass

    def acc(self, y, y_pred):
        pass


class SquareLoss(Loss):
    """Hoàn thiện class SquareLoss từ đầu."""
    def __init__(self):
        pass

    def loss(self, y, y_pred):
        pass

    def gradient(self, y, y_pred):
        pass


class CrossEntropy(Loss):
    """Hoàn thiện class CrossEntropy từ đầu."""
    def __init__(self):
        pass

    def loss(self, y, p):
        pass

    def acc(self, y, p):
        pass

    def gradient(self, y, p):
        pass
