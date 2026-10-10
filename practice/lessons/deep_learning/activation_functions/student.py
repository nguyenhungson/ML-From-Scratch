"""BÀI THỰC HÀNH ĐỘC LẬP - deep_learning/activation_functions
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class Sigmoid:
    """Hoàn thiện class Sigmoid từ đầu."""
    def __call__(self, x):
        """Sigmoid.__call__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Sigmoid.__call__")

    def gradient(self, x):
        """Sigmoid.gradient: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Sigmoid.gradient")


class Softmax:
    """Hoàn thiện class Softmax từ đầu."""
    def __call__(self, x):
        """Softmax.__call__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Softmax.__call__")

    def gradient(self, x):
        """Softmax.gradient: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Softmax.gradient")


class TanH:
    """Hoàn thiện class TanH từ đầu."""
    def __call__(self, x):
        """TanH.__call__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: TanH.__call__")

    def gradient(self, x):
        """TanH.gradient: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: TanH.gradient")


class ReLU:
    """Hoàn thiện class ReLU từ đầu."""
    def __call__(self, x):
        """ReLU.__call__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ReLU.__call__")

    def gradient(self, x):
        """ReLU.gradient: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ReLU.gradient")


class LeakyReLU:
    """Hoàn thiện class LeakyReLU từ đầu."""
    def __init__(self, alpha=0.2):
        """LeakyReLU.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LeakyReLU.__init__")

    def __call__(self, x):
        """LeakyReLU.__call__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LeakyReLU.__call__")

    def gradient(self, x):
        """LeakyReLU.gradient: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: LeakyReLU.gradient")


class ELU:
    """Hoàn thiện class ELU từ đầu."""
    def __init__(self, alpha=0.1):
        """ELU.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ELU.__init__")

    def __call__(self, x):
        """ELU.__call__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ELU.__call__")

    def gradient(self, x):
        """ELU.gradient: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ELU.gradient")


class SELU:
    """Hoàn thiện class SELU từ đầu."""
    def __init__(self):
        """SELU.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: SELU.__init__")

    def __call__(self, x):
        """SELU.__call__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: SELU.__call__")

    def gradient(self, x):
        """SELU.gradient: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: SELU.gradient")


class SoftPlus:
    """Hoàn thiện class SoftPlus từ đầu."""
    def __call__(self, x):
        """SoftPlus.__call__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: SoftPlus.__call__")

    def gradient(self, x):
        """SoftPlus.gradient: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: SoftPlus.gradient")
