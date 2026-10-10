"""BÀI THỰC HÀNH ĐỘC LẬP - supervised_learning/neuroevolution
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class Neuroevolution:
    """Hoàn thiện class Neuroevolution từ đầu."""
    def __init__(self, population_size, mutation_rate, model_builder):
        """Neuroevolution.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Neuroevolution.__init__")

    def _build_model(self, id):
        """Neuroevolution._build_model: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Neuroevolution._build_model")

    def _initialize_population(self):
        """Neuroevolution._initialize_population: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Neuroevolution._initialize_population")

    def _mutate(self, individual, var=1):
        """Neuroevolution._mutate: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Neuroevolution._mutate")

    def _inherit_weights(self, child, parent):
        """Neuroevolution._inherit_weights: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Neuroevolution._inherit_weights")

    def _crossover(self, parent1, parent2):
        """Neuroevolution._crossover: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Neuroevolution._crossover")

    def _calculate_fitness(self):
        """Neuroevolution._calculate_fitness: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Neuroevolution._calculate_fitness")

    def evolve(self, X, y, n_generations):
        """Neuroevolution.evolve: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: Neuroevolution.evolve")
