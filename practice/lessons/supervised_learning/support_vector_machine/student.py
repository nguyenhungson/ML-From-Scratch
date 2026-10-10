"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/support_vector_machine
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class SupportVectorMachine(object):
    """Hoàn thiện class SupportVectorMachine từ đầu."""
    def __init__(self, C=1, kernel=None, power=4, gamma=None, coef=4):
        """SupportVectorMachine.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: SupportVectorMachine.__init__")

    def fit(self, X, y):
        """SupportVectorMachine.fit: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: SupportVectorMachine.fit")

    def predict(self, X):
        """SupportVectorMachine.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: SupportVectorMachine.predict")
