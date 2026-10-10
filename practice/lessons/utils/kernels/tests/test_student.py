"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s,"linear_kernel",None)))
        self.assertTrue(callable(getattr(s,"polynomial_kernel",None)))
        self.assertTrue(callable(getattr(s,"rbf_kernel",None)))

    def test_linear(self):
        X=np.array([[1.,2.],[2.,3.]])
        result=s.linear_kernel()(X,X)
        np.testing.assert_allclose(result,X@X.T,rtol=1e-6)
    def test_rbf_symmetry(self):
        X=np.array([[0.,0.],[1.,0.]])
        f=s.rbf_kernel(gamma=1.)
        K=np.array([[f(a,b) for b in X] for a in X])
        np.testing.assert_allclose(K,K.T,atol=1e-8)
        np.testing.assert_allclose(np.diag(K),np.ones(2),atol=1e-8)
        self.assertAlmostEqual(float(f(X[0],X[1])),np.exp(-1.),places=6)
