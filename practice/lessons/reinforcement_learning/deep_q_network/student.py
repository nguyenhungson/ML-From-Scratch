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
        pass

    def set_model(self, model):
        pass

    def _select_action(self, state):
        pass

    def _memorize(self, state, action, reward, new_state, done):
        pass

    def _construct_training_set(self, replay):
        pass

    def train(self, n_epochs=500, batch_size=32):
        pass

    def play(self, n_epochs):
        pass
