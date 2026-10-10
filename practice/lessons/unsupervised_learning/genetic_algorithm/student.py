"""BÀI THỰC HÀNH ĐỘC LẬP - unsupervised_learning/genetic_algorithm
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class GeneticAlgorithm:
    """Hoàn thiện class GeneticAlgorithm từ đầu."""
    def __init__(self, target_string, population_size, mutation_rate):
        """GeneticAlgorithm.__init__: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GeneticAlgorithm.__init__")

    def _initialize(self):
        """GeneticAlgorithm._initialize: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GeneticAlgorithm._initialize")

    def _calculate_fitness(self):
        """GeneticAlgorithm._calculate_fitness: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GeneticAlgorithm._calculate_fitness")

    def _mutate(self, individual):
        """GeneticAlgorithm._mutate: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GeneticAlgorithm._mutate")

    def _crossover(self, parent1, parent2):
        """GeneticAlgorithm._crossover: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GeneticAlgorithm._crossover")

    def run(self, iterations):
        """GeneticAlgorithm.run: tự cài đặt theo README.md. Không sao chép mã tham khảo trước khi làm."""
        raise NotImplementedError("TODO: GeneticAlgorithm.run")
