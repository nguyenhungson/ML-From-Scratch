"""BÀI THỰC HÀNH ĐỘC LẬP - utils/data_manipulation
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

def shuffle_data(X, y, seed=None):
    pass

def batch_iterator(X, y=None, batch_size=64):
    pass

def divide_on_feature(X, feature_i, threshold):
    pass

def polynomial_features(X, degree):
    pass

def get_random_subsets(X, y, n_subsets, replacements=True):
    pass

def normalize(X, axis=-1, order=2):
    pass

def standardize(X):
    pass

def train_test_split(X, y, test_size=0.5, shuffle=True, seed=None):
    pass

def k_fold_cross_validation_sets(X, y, k, shuffle=True):
    pass

def to_categorical(x, n_col=None):
    pass

def to_nominal(x):
    pass

def make_diagonal(x):
    pass
