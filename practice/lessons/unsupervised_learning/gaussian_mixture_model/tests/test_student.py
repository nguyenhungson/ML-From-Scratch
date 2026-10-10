"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.GaussianMixtureModel,"__init__",None)))
        self.assertTrue(callable(getattr(s.GaussianMixtureModel,"multivariate_gaussian",None)))
        self.assertTrue(callable(getattr(s.GaussianMixtureModel,"predict",None)))

    def test_separated_gaussians(self):
        np.random.seed(0)
        X=np.array([[-4.,-4.],[-4.,-3.],[-3.,-4.],[3.,3.],[3.,4.],[4.,3.]])
        label=np.asarray(s.GaussianMixtureModel(k=2,max_iterations=100).predict(X)).ravel()
        self.assertEqual(label.shape,(6,))
        self.assertEqual(len(set(label[:3])),1)
        self.assertNotEqual(label[0],label[3])
