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
        """Plot.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Plot.__init__")

    def _transform(self, X, dim):
        """Plot._transform: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Plot._transform")

    def plot_regression(self, lines, title, axis_labels=None, mse=None, scatter=None, legend={'type': 'lines', 'loc': 'lower right'}):
        """Plot.plot_regression: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Plot.plot_regression")

    def plot_in_2d(self, X, y=None, title=None, accuracy=None, legend_labels=None):
        """Plot.plot_in_2d: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Plot.plot_in_2d")

    def plot_in_3d(self, X, y=None):
        """Plot.plot_in_3d: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Plot.plot_in_3d")
