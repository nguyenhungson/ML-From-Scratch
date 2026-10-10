"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.DecisionStump,"__init__",None)))
        self.assertTrue(callable(getattr(s.Adaboost,"__init__",None)))
        self.assertTrue(callable(getattr(s.Adaboost,"fit",None)))
        self.assertTrue(callable(getattr(s.Adaboost,"predict",None)))
        self.assertTrue(callable(getattr(s,"main",None)))

    def test_binary(self):
        X=np.array([[0.],[1.],[2.],[3.],[4.],[5.]])
        y=np.array([-1,-1,-1,1,1,1]);m=s.Adaboost(n_clf=5)
        m.fit(X,y);pred=np.asarray(m.predict(X)).ravel()
        self.assertEqual(pred.shape,y.shape)
        self.assertGreaterEqual(np.mean(pred==y),0.8)
