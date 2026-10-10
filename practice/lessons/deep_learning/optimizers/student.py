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
        """StochasticGradientDescent.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: StochasticGradientDescent.__init__")

    def update(self, w, grad_wrt_w):
        """StochasticGradientDescent.update: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: StochasticGradientDescent.update")


class NesterovAcceleratedGradient:
    """Hoàn thiện class NesterovAcceleratedGradient từ đầu."""
    def __init__(self, learning_rate=0.001, momentum=0.4):
        """NesterovAcceleratedGradient.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NesterovAcceleratedGradient.__init__")

    def update(self, w, grad_func):
        """NesterovAcceleratedGradient.update: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: NesterovAcceleratedGradient.update")


class Adagrad:
    """Hoàn thiện class Adagrad từ đầu."""
    def __init__(self, learning_rate=0.01):
        """Adagrad.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Adagrad.__init__")

    def update(self, w, grad_wrt_w):
        """Adagrad.update: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Adagrad.update")


class Adadelta:
    """Hoàn thiện class Adadelta từ đầu."""
    def __init__(self, rho=0.95, eps=1e-06):
        """Adadelta.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Adadelta.__init__")

    def update(self, w, grad_wrt_w):
        """Adadelta.update: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Adadelta.update")


class RMSprop:
    """Hoàn thiện class RMSprop từ đầu."""
    def __init__(self, learning_rate=0.01, rho=0.9):
        """RMSprop.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RMSprop.__init__")

    def update(self, w, grad_wrt_w):
        """RMSprop.update: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RMSprop.update")


class Adam:
    """Hoàn thiện class Adam từ đầu."""
    def __init__(self, learning_rate=0.001, b1=0.9, b2=0.999):
        """Adam.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Adam.__init__")

    def update(self, w, grad_wrt_w):
        """Adam.update: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Adam.update")
