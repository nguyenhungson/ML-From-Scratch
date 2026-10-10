"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/multi_class_lda
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class MultiClassLDA:
    """Hoàn thiện class MultiClassLDA từ đầu."""
    def __init__(self, solver='svd'):
        """MultiClassLDA.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: MultiClassLDA.__init__")

    def _calculate_scatter_matrices(self, X, y):
        """MultiClassLDA._calculate_scatter_matrices: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: MultiClassLDA._calculate_scatter_matrices")

    def transform(self, X, y, n_components):
        """MultiClassLDA.transform: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: MultiClassLDA.transform")

    def plot_in_2d(self, X, y, title=None):
        """MultiClassLDA.plot_in_2d: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: MultiClassLDA.plot_in_2d")
