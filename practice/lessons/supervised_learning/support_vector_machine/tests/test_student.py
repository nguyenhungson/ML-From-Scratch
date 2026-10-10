"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.SupportVectorMachine,"__init__",None)))
        self.assertTrue(callable(getattr(s.SupportVectorMachine,"fit",None)))
        self.assertTrue(callable(getattr(s.SupportVectorMachine,"predict",None)))

    def test_binary_margin(self):
        X=np.array([[-2.,-2.],[-3.,-1.],[2.,2.],[3.,1.]])
        y=np.array([-1,-1,1,1]);m=s.SupportVectorMachine(C=1)
        m.fit(X,y);pred=np.asarray(m.predict(X)).ravel()
        self.assertEqual(pred.shape,y.shape)
        self.assertGreaterEqual(np.mean(pred==y),0.75)
