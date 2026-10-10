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
        """Layer.set_input_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Layer.set_input_shape")

    def layer_name(self):
        """Layer.layer_name: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Layer.layer_name")

    def parameters(self):
        """Layer.parameters: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Layer.parameters")

    def forward_pass(self, X, training):
        """Layer.forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Layer.forward_pass")

    def backward_pass(self, accum_grad):
        """Layer.backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Layer.backward_pass")

    def output_shape(self):
        """Layer.output_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Layer.output_shape")


class Dense(Layer):
    """Hoàn thiện class Dense từ đầu."""
    def __init__(self, n_units, input_shape=None):
        """Dense.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Dense.__init__")

    def initialize(self, optimizer):
        """Dense.initialize: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Dense.initialize")

    def parameters(self):
        """Dense.parameters: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Dense.parameters")

    def forward_pass(self, X, training=True):
        """Dense.forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Dense.forward_pass")

    def backward_pass(self, accum_grad):
        """Dense.backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Dense.backward_pass")

    def output_shape(self):
        """Dense.output_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Dense.output_shape")


class RNN(Layer):
    """Hoàn thiện class RNN từ đầu."""
    def __init__(self, n_units, activation='tanh', bptt_trunc=5, input_shape=None):
        """RNN.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RNN.__init__")

    def initialize(self, optimizer):
        """RNN.initialize: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RNN.initialize")

    def parameters(self):
        """RNN.parameters: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RNN.parameters")

    def forward_pass(self, X, training=True):
        """RNN.forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RNN.forward_pass")

    def backward_pass(self, accum_grad):
        """RNN.backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RNN.backward_pass")

    def output_shape(self):
        """RNN.output_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: RNN.output_shape")


class Conv2D(Layer):
    """Hoàn thiện class Conv2D từ đầu."""
    def __init__(self, n_filters, filter_shape, input_shape=None, padding='same', stride=1):
        """Conv2D.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Conv2D.__init__")

    def initialize(self, optimizer):
        """Conv2D.initialize: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Conv2D.initialize")

    def parameters(self):
        """Conv2D.parameters: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Conv2D.parameters")

    def forward_pass(self, X, training=True):
        """Conv2D.forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Conv2D.forward_pass")

    def backward_pass(self, accum_grad):
        """Conv2D.backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Conv2D.backward_pass")

    def output_shape(self):
        """Conv2D.output_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Conv2D.output_shape")


class BatchNormalization(Layer):
    """Hoàn thiện class BatchNormalization từ đầu."""
    def __init__(self, momentum=0.99):
        """BatchNormalization.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: BatchNormalization.__init__")

    def initialize(self, optimizer):
        """BatchNormalization.initialize: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: BatchNormalization.initialize")

    def parameters(self):
        """BatchNormalization.parameters: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: BatchNormalization.parameters")

    def forward_pass(self, X, training=True):
        """BatchNormalization.forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: BatchNormalization.forward_pass")

    def backward_pass(self, accum_grad):
        """BatchNormalization.backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: BatchNormalization.backward_pass")

    def output_shape(self):
        """BatchNormalization.output_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: BatchNormalization.output_shape")


class PoolingLayer(Layer):
    """Hoàn thiện class PoolingLayer từ đầu."""
    def __init__(self, pool_shape=(2, 2), stride=1, padding=0):
        """PoolingLayer.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PoolingLayer.__init__")

    def forward_pass(self, X, training=True):
        """PoolingLayer.forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PoolingLayer.forward_pass")

    def backward_pass(self, accum_grad):
        """PoolingLayer.backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PoolingLayer.backward_pass")

    def output_shape(self):
        """PoolingLayer.output_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: PoolingLayer.output_shape")


class MaxPooling2D(PoolingLayer):
    """Hoàn thiện class MaxPooling2D từ đầu."""
    def _pool_forward(self, X_col):
        """MaxPooling2D._pool_forward: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: MaxPooling2D._pool_forward")

    def _pool_backward(self, accum_grad):
        """MaxPooling2D._pool_backward: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: MaxPooling2D._pool_backward")


class AveragePooling2D(PoolingLayer):
    """Hoàn thiện class AveragePooling2D từ đầu."""
    def _pool_forward(self, X_col):
        """AveragePooling2D._pool_forward: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: AveragePooling2D._pool_forward")

    def _pool_backward(self, accum_grad):
        """AveragePooling2D._pool_backward: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: AveragePooling2D._pool_backward")


class ConstantPadding2D(Layer):
    """Hoàn thiện class ConstantPadding2D từ đầu."""
    def __init__(self, padding, padding_value=0):
        """ConstantPadding2D.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ConstantPadding2D.__init__")

    def forward_pass(self, X, training=True):
        """ConstantPadding2D.forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ConstantPadding2D.forward_pass")

    def backward_pass(self, accum_grad):
        """ConstantPadding2D.backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ConstantPadding2D.backward_pass")

    def output_shape(self):
        """ConstantPadding2D.output_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ConstantPadding2D.output_shape")


class ZeroPadding2D(ConstantPadding2D):
    """Hoàn thiện class ZeroPadding2D từ đầu."""
    def __init__(self, padding):
        """ZeroPadding2D.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: ZeroPadding2D.__init__")


class Flatten(Layer):
    """Hoàn thiện class Flatten từ đầu."""
    def __init__(self, input_shape=None):
        """Flatten.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Flatten.__init__")

    def forward_pass(self, X, training=True):
        """Flatten.forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Flatten.forward_pass")

    def backward_pass(self, accum_grad):
        """Flatten.backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Flatten.backward_pass")

    def output_shape(self):
        """Flatten.output_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Flatten.output_shape")


class UpSampling2D(Layer):
    """Hoàn thiện class UpSampling2D từ đầu."""
    def __init__(self, size=(2, 2), input_shape=None):
        """UpSampling2D.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: UpSampling2D.__init__")

    def forward_pass(self, X, training=True):
        """UpSampling2D.forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: UpSampling2D.forward_pass")

    def backward_pass(self, accum_grad):
        """UpSampling2D.backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: UpSampling2D.backward_pass")

    def output_shape(self):
        """UpSampling2D.output_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: UpSampling2D.output_shape")


class Reshape(Layer):
    """Hoàn thiện class Reshape từ đầu."""
    def __init__(self, shape, input_shape=None):
        """Reshape.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Reshape.__init__")

    def forward_pass(self, X, training=True):
        """Reshape.forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Reshape.forward_pass")

    def backward_pass(self, accum_grad):
        """Reshape.backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Reshape.backward_pass")

    def output_shape(self):
        """Reshape.output_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Reshape.output_shape")


class Dropout(Layer):
    """Hoàn thiện class Dropout từ đầu."""
    def __init__(self, p=0.2):
        """Dropout.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Dropout.__init__")

    def forward_pass(self, X, training=True):
        """Dropout.forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Dropout.forward_pass")

    def backward_pass(self, accum_grad):
        """Dropout.backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Dropout.backward_pass")

    def output_shape(self):
        """Dropout.output_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Dropout.output_shape")


class Activation(Layer):
    """Hoàn thiện class Activation từ đầu."""
    def __init__(self, name):
        """Activation.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Activation.__init__")

    def layer_name(self):
        """Activation.layer_name: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Activation.layer_name")

    def forward_pass(self, X, training=True):
        """Activation.forward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Activation.forward_pass")

    def backward_pass(self, accum_grad):
        """Activation.backward_pass: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Activation.backward_pass")

    def output_shape(self):
        """Activation.output_shape: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Activation.output_shape")


def determine_padding(filter_shape, output_shape='same'):
    """determine_padding: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: determine_padding")

def get_im2col_indices(images_shape, filter_shape, padding, stride=1):
    """get_im2col_indices: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: get_im2col_indices")

def image_to_column(images, filter_shape, stride, output_shape='same'):
    """image_to_column: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: image_to_column")

def column_to_image(cols, images_shape, filter_shape, stride, output_shape='same'):
    """column_to_image: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
    raise NotImplementedError("TODO: column_to_image")
