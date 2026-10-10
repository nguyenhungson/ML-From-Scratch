"""BÀI THỰC HÀNH ĐỘC LẬP - utils/data_manipulation
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

def shuffle_data(X, y, seed=None):
    """shuffle_data: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: shuffle_data")

def batch_iterator(X, y=None, batch_size=64):
    """batch_iterator: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: batch_iterator")

def divide_on_feature(X, feature_i, threshold):
    """divide_on_feature: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: divide_on_feature")

def polynomial_features(X, degree):
    """polynomial_features: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: polynomial_features")

def get_random_subsets(X, y, n_subsets, replacements=True):
    """get_random_subsets: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: get_random_subsets")

def normalize(X, axis=-1, order=2):
    """normalize: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: normalize")

def standardize(X):
    """standardize: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: standardize")

def train_test_split(X, y, test_size=0.5, shuffle=True, seed=None):
    """train_test_split: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: train_test_split")

def k_fold_cross_validation_sets(X, y, k, shuffle=True):
    """k_fold_cross_validation_sets: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: k_fold_cross_validation_sets")

def to_categorical(x, n_col=None):
    """to_categorical: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: to_categorical")

def to_nominal(x):
    """to_nominal: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: to_nominal")

def make_diagonal(x):
    """make_diagonal: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: make_diagonal")
