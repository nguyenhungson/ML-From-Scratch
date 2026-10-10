"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.GeneticAlgorithm,"__init__",None)))
        self.assertTrue(callable(getattr(s.GeneticAlgorithm,"run",None)))

    def test_fitness_or_solution(self):
        np.random.seed(0)
        m=s.GeneticAlgorithm(target_string='ABC',population_size=50,mutation_rate=.1)
        self.assertIsNotNone(m.run(iterations=50))
