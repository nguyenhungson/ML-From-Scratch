"""BÀI THỰC HÀNH ĐỘC LẬP - unsupervised_learning/gaussian_mixture_model
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class GaussianMixtureModel:
    """Hoàn thiện class GaussianMixtureModel từ đầu."""
    def __init__(self, k=2, max_iterations=2000, tolerance=1e-08):
        """GaussianMixtureModel.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GaussianMixtureModel.__init__")

    def _init_random_gaussians(self, X):
        """GaussianMixtureModel._init_random_gaussians: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GaussianMixtureModel._init_random_gaussians")

    def multivariate_gaussian(self, X, params):
        """GaussianMixtureModel.multivariate_gaussian: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GaussianMixtureModel.multivariate_gaussian")

    def _get_likelihoods(self, X):
        """GaussianMixtureModel._get_likelihoods: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GaussianMixtureModel._get_likelihoods")

    def _expectation(self, X):
        """GaussianMixtureModel._expectation: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GaussianMixtureModel._expectation")

    def _maximization(self, X):
        """GaussianMixtureModel._maximization: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GaussianMixtureModel._maximization")

    def _converged(self, X):
        """GaussianMixtureModel._converged: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GaussianMixtureModel._converged")

    def predict(self, X):
        """GaussianMixtureModel.predict: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GaussianMixtureModel.predict")
