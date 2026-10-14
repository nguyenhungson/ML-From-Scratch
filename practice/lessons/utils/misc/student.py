"""BÀI THỰC HÀNH ĐỘC LẬP - utils/misc
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class Plot:
    """Hoàn thiện class Plot từ đầu."""
    def __init__(self):
        pass

    def _transform(self, X, dim):
        pass

    def plot_regression(self, lines, title, axis_labels=None, mse=None, scatter=None, legend={'type': 'lines', 'loc': 'lower right'}):
        pass

    def plot_in_2d(self, X, y=None, title=None, accuracy=None, legend_labels=None):
        pass

    def plot_in_3d(self, X, y=None):
        pass
