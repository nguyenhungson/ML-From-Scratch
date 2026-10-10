"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s,"calculate_entropy",None)))
        self.assertTrue(callable(getattr(s,"mean_squared_error",None)))
        self.assertTrue(callable(getattr(s,"calculate_variance",None)))
        self.assertTrue(callable(getattr(s,"calculate_std_dev",None)))
        self.assertTrue(callable(getattr(s,"euclidean_distance",None)))
        self.assertTrue(callable(getattr(s,"accuracy_score",None)))
        self.assertTrue(callable(getattr(s,"calculate_covariance_matrix",None)))
        self.assertTrue(callable(getattr(s,"calculate_correlation_matrix",None)))

    def test_distance_and_mse(self):
        self.assertAlmostEqual(float(s.euclidean_distance(np.array([0.,0.]),np.array([3.,4.]))),5.0)
        self.assertAlmostEqual(float(s.mean_squared_error(np.array([1.,2.]),np.array([1.,2.]))),0.0)
    def test_entropy(self):
        self.assertAlmostEqual(float(s.calculate_entropy(np.array([0,0,1,1]))),1.0,places=6)
