"""BÀI THỰC HÀNH ĐỘC LẬP - reinforcement_learning/deep_q_network
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class DeepQNetwork:
    """Hoàn thiện class DeepQNetwork từ đầu."""
    def __init__(self, env_name='CartPole-v1', epsilon=1, gamma=0.9, decay_rate=0.005, min_epsilon=0.1):
        """DeepQNetwork.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DeepQNetwork.__init__")

    def set_model(self, model):
        """DeepQNetwork.set_model: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DeepQNetwork.set_model")

    def _select_action(self, state):
        """DeepQNetwork._select_action: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DeepQNetwork._select_action")

    def _memorize(self, state, action, reward, new_state, done):
        """DeepQNetwork._memorize: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DeepQNetwork._memorize")

    def _construct_training_set(self, replay):
        """DeepQNetwork._construct_training_set: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DeepQNetwork._construct_training_set")

    def train(self, n_epochs=500, batch_size=32):
        """DeepQNetwork.train: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DeepQNetwork.train")

    def play(self, n_epochs):
        """DeepQNetwork.play: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: DeepQNetwork.play")
