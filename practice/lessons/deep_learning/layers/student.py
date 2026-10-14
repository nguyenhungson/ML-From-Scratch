"""BÀI THỰC HÀNH ĐỘC LẬP - deep_learning/layers
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class Layer(object):
    """Hoàn thiện class Layer từ đầu."""
    def set_input_shape(self, shape):
        pass

    def layer_name(self):
        pass

    def parameters(self):
        pass

    def forward_pass(self, X, training):
        pass

    def backward_pass(self, accum_grad):
        pass

    def output_shape(self):
        pass


class Dense(Layer):
    """Hoàn thiện class Dense từ đầu."""
    def __init__(self, n_units, input_shape=None):
        pass

    def initialize(self, optimizer):
        pass

    def parameters(self):
        pass

    def forward_pass(self, X, training=True):
        pass

    def backward_pass(self, accum_grad):
        pass

    def output_shape(self):
        pass


class RNN(Layer):
    """Hoàn thiện class RNN từ đầu."""
    def __init__(self, n_units, activation='tanh', bptt_trunc=5, input_shape=None):
        pass

    def initialize(self, optimizer):
        pass

    def parameters(self):
        pass

    def forward_pass(self, X, training=True):
        pass

    def backward_pass(self, accum_grad):
        pass

    def output_shape(self):
        pass


class Conv2D(Layer):
    """Hoàn thiện class Conv2D từ đầu."""
    def __init__(self, n_filters, filter_shape, input_shape=None, padding='same', stride=1):
        pass

    def initialize(self, optimizer):
        pass

    def parameters(self):
        pass

    def forward_pass(self, X, training=True):
        pass

    def backward_pass(self, accum_grad):
        pass

    def output_shape(self):
        pass


class BatchNormalization(Layer):
    """Hoàn thiện class BatchNormalization từ đầu."""
    def __init__(self, momentum=0.99):
        pass

    def initialize(self, optimizer):
        pass

    def parameters(self):
        pass

    def forward_pass(self, X, training=True):
        pass

    def backward_pass(self, accum_grad):
        pass

    def output_shape(self):
        pass


class PoolingLayer(Layer):
    """Hoàn thiện class PoolingLayer từ đầu."""
    def __init__(self, pool_shape=(2, 2), stride=1, padding=0):
        pass

    def forward_pass(self, X, training=True):
        pass

    def backward_pass(self, accum_grad):
        pass

    def output_shape(self):
        pass


class MaxPooling2D(PoolingLayer):
    """Hoàn thiện class MaxPooling2D từ đầu."""
    def _pool_forward(self, X_col):
        pass

    def _pool_backward(self, accum_grad):
        pass


class AveragePooling2D(PoolingLayer):
    """Hoàn thiện class AveragePooling2D từ đầu."""
    def _pool_forward(self, X_col):
        pass

    def _pool_backward(self, accum_grad):
        pass


class ConstantPadding2D(Layer):
    """Hoàn thiện class ConstantPadding2D từ đầu."""
    def __init__(self, padding, padding_value=0):
        pass

    def forward_pass(self, X, training=True):
        pass

    def backward_pass(self, accum_grad):
        pass

    def output_shape(self):
        pass


class ZeroPadding2D(ConstantPadding2D):
    """Hoàn thiện class ZeroPadding2D từ đầu."""
    def __init__(self, padding):
        pass


class Flatten(Layer):
    """Hoàn thiện class Flatten từ đầu."""
    def __init__(self, input_shape=None):
        pass

    def forward_pass(self, X, training=True):
        pass

    def backward_pass(self, accum_grad):
        pass

    def output_shape(self):
        pass


class UpSampling2D(Layer):
    """Hoàn thiện class UpSampling2D từ đầu."""
    def __init__(self, size=(2, 2), input_shape=None):
        pass

    def forward_pass(self, X, training=True):
        pass

    def backward_pass(self, accum_grad):
        pass

    def output_shape(self):
        pass


class Reshape(Layer):
    """Hoàn thiện class Reshape từ đầu."""
    def __init__(self, shape, input_shape=None):
        pass

    def forward_pass(self, X, training=True):
        pass

    def backward_pass(self, accum_grad):
        pass

    def output_shape(self):
        pass


class Dropout(Layer):
    """Hoàn thiện class Dropout từ đầu."""
    def __init__(self, p=0.2):
        pass

    def forward_pass(self, X, training=True):
        pass

    def backward_pass(self, accum_grad):
        pass

    def output_shape(self):
        pass


class Activation(Layer):
    """Hoàn thiện class Activation từ đầu."""
    def __init__(self, name):
        pass

    def layer_name(self):
        pass

    def forward_pass(self, X, training=True):
        pass

    def backward_pass(self, accum_grad):
        pass

    def output_shape(self):
        pass


def determine_padding(filter_shape, output_shape='same'):
    pass

def get_im2col_indices(images_shape, filter_shape, padding, stride=1):
    pass

def image_to_column(images, filter_shape, stride, output_shape='same'):
    pass

def column_to_image(cols, images_shape, filter_shape, stride, output_shape='same'):
    pass
