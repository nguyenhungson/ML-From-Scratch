"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.RandomForest,"__init__",None)))
        self.assertTrue(callable(getattr(s.RandomForest,"fit",None)))
        self.assertTrue(callable(getattr(s.RandomForest,"predict",None)))

    def test_toy_labels(self):
        np.random.seed(1)
        X=np.array([[-2.],[-1.5],[-1.],[-0.5],[.5],[1.],[1.5],[2.]])
        y=np.array([0,0,0,0,1,1,1,1]);m=s.RandomForest(n_estimators=9,max_depth=3)
        m.fit(X,y)
        pred=np.asarray(m.predict(X)).ravel()
        self.assertEqual(pred.shape,y.shape)
        self.assertGreaterEqual(np.mean(pred==y),0.75)
