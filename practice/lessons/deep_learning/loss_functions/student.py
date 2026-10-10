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
        """Loss.loss: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Loss.loss")

    def gradient(self, y, y_pred):
        """Loss.gradient: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Loss.gradient")

    def acc(self, y, y_pred):
        """Loss.acc: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Loss.acc")


class SquareLoss(Loss):
    """Hoàn thiện class SquareLoss từ đầu."""
    def __init__(self):
        """SquareLoss.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: SquareLoss.__init__")

    def loss(self, y, y_pred):
        """SquareLoss.loss: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: SquareLoss.loss")

    def gradient(self, y, y_pred):
        """SquareLoss.gradient: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: SquareLoss.gradient")


class CrossEntropy(Loss):
    """Hoàn thiện class CrossEntropy từ đầu."""
    def __init__(self):
        """CrossEntropy.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: CrossEntropy.__init__")

    def loss(self, y, p):
        """CrossEntropy.loss: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: CrossEntropy.loss")

    def acc(self, y, p):
        """CrossEntropy.acc: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: CrossEntropy.acc")

    def gradient(self, y, p):
        """CrossEntropy.gradient: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: CrossEntropy.gradient")
