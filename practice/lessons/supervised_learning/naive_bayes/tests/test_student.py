"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.NaiveBayes,"fit",None)))
        self.assertTrue(callable(getattr(s.NaiveBayes,"predict",None)))

    def test_two_classes(self):
        X=np.array([[-4.,-3.],[-3.,-4.],[-2.,-3.],[2.,3.],[3.,4.],[4.,3.]])
        y=np.array([0,0,0,1,1,1]);m=s.NaiveBayes();m.fit(X,y)
        self.assertGreaterEqual(np.mean(np.asarray(m.predict(X)).reshape(-1)==y),0.95)
