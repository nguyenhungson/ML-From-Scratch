"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.Loss,"loss",None)))
        self.assertTrue(callable(getattr(s.Loss,"gradient",None)))
        self.assertTrue(callable(getattr(s.Loss,"acc",None)))
        self.assertTrue(callable(getattr(s.SquareLoss,"__init__",None)))
        self.assertTrue(callable(getattr(s.SquareLoss,"loss",None)))
        self.assertTrue(callable(getattr(s.SquareLoss,"gradient",None)))
        self.assertTrue(callable(getattr(s.CrossEntropy,"__init__",None)))
        self.assertTrue(callable(getattr(s.CrossEntropy,"loss",None)))
        self.assertTrue(callable(getattr(s.CrossEntropy,"acc",None)))
        self.assertTrue(callable(getattr(s.CrossEntropy,"gradient",None)))

    def test_mse(self):
        m=s.SquareLoss()
        v=np.asarray(m.loss(np.array([1.,2.]),np.array([1.,2.])))
        self.assertAlmostEqual(float(np.mean(v)),0.)
    def test_crossentropy_order(self):
        ce=s.CrossEntropy();y=np.array([[1.,0.]])
        good=np.mean(ce.loss(y,np.array([[.9,.1]])))
        bad=np.mean(ce.loss(y,np.array([[.1,.9]])))
        self.assertLess(good,bad)
