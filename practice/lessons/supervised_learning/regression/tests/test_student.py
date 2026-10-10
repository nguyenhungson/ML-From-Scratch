"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.l1_regularization,"__init__",None)))
        self.assertTrue(callable(getattr(s.l1_regularization,"grad",None)))
        self.assertTrue(callable(getattr(s.l2_regularization,"__init__",None)))
        self.assertTrue(callable(getattr(s.l2_regularization,"grad",None)))
        self.assertTrue(callable(getattr(s.l1_l2_regularization,"__init__",None)))
        self.assertTrue(callable(getattr(s.l1_l2_regularization,"grad",None)))
        self.assertTrue(callable(getattr(s.Regression,"__init__",None)))
        self.assertTrue(callable(getattr(s.Regression,"initialize_weights",None)))
        self.assertTrue(callable(getattr(s.Regression,"fit",None)))
        self.assertTrue(callable(getattr(s.Regression,"predict",None)))
        self.assertTrue(callable(getattr(s.LinearRegression,"__init__",None)))
        self.assertTrue(callable(getattr(s.LinearRegression,"fit",None)))
        self.assertTrue(callable(getattr(s.LassoRegression,"__init__",None)))
        self.assertTrue(callable(getattr(s.LassoRegression,"fit",None)))
        self.assertTrue(callable(getattr(s.LassoRegression,"predict",None)))
        self.assertTrue(callable(getattr(s.PolynomialRegression,"__init__",None)))
        self.assertTrue(callable(getattr(s.PolynomialRegression,"fit",None)))
        self.assertTrue(callable(getattr(s.PolynomialRegression,"predict",None)))
        self.assertTrue(callable(getattr(s.RidgeRegression,"__init__",None)))
        self.assertTrue(callable(getattr(s.PolynomialRidgeRegression,"__init__",None)))
        self.assertTrue(callable(getattr(s.PolynomialRidgeRegression,"fit",None)))
        self.assertTrue(callable(getattr(s.PolynomialRidgeRegression,"predict",None)))
        self.assertTrue(callable(getattr(s.ElasticNet,"__init__",None)))
        self.assertTrue(callable(getattr(s.ElasticNet,"fit",None)))
        self.assertTrue(callable(getattr(s.ElasticNet,"predict",None)))

    def test_linear_fit(self):
        X=np.arange(1,6,dtype=float).reshape(-1,1)
        y=2*X.ravel()+1
        m=s.LinearRegression(n_iterations=3000,learning_rate=0.01,gradient_descent=True)
        m.fit(X,y)
        pred=np.asarray(m.predict(X)).ravel()
        np.testing.assert_allclose(pred,y,atol=0.6)
