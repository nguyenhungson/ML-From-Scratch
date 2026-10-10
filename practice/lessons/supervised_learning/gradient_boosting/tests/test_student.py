"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.GradientBoosting,"__init__",None)))
        self.assertTrue(callable(getattr(s.GradientBoosting,"fit",None)))
        self.assertTrue(callable(getattr(s.GradientBoosting,"predict",None)))
        self.assertTrue(callable(getattr(s.GradientBoostingRegressor,"__init__",None)))
        self.assertTrue(callable(getattr(s.GradientBoostingClassifier,"__init__",None)))
        self.assertTrue(callable(getattr(s.GradientBoostingClassifier,"fit",None)))

    def test_regression(self):
        X=np.arange(10,dtype=float).reshape(-1,1)
        y=X.ravel()**2
        m=s.GradientBoostingRegressor(n_estimators=50,max_depth=2,learning_rate=0.1)
        m.fit(X,y);pred=np.asarray(m.predict(X)).ravel()
        self.assertLess(np.mean((pred-y)**2),10.)
