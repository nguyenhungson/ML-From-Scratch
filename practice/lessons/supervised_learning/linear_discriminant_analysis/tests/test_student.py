"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.LDA,"__init__",None)))
        self.assertTrue(callable(getattr(s.LDA,"transform",None)))
        self.assertTrue(callable(getattr(s.LDA,"fit",None)))
        self.assertTrue(callable(getattr(s.LDA,"predict",None)))

    def test_binary(self):
        X=np.array([[-3.,-2.],[-2.,-1.],[-4.,-2.],[2.,3.],[3.,2.],[4.,2.]])
        y=np.array([0,0,0,1,1,1]);m=s.LDA()
        m.fit(X,y);pred=np.asarray(m.predict(X)).ravel()
        self.assertGreaterEqual(np.mean(pred==y),0.8)
