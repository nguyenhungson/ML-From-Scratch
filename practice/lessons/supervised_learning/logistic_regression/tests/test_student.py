"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.LogisticRegression,"__init__",None)))
        self.assertTrue(callable(getattr(s.LogisticRegression,"fit",None)))
        self.assertTrue(callable(getattr(s.LogisticRegression,"predict",None)))

    def test_separable(self):
        X=np.array([[-3.,-2.],[-2.,-1.],[-1.,-3.],[2.,3.],[3.,2.],[1.,3.]])
        y=np.array([0,0,0,1,1,1])
        m=s.LogisticRegression(learning_rate=0.1)
        m.fit(X,y,n_iterations=500)
        self.assertGreaterEqual(np.mean(np.asarray(m.predict(X)).reshape(-1)==y),0.95)
