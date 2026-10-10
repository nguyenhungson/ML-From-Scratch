"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.StochasticGradientDescent,"__init__",None)))
        self.assertTrue(callable(getattr(s.StochasticGradientDescent,"update",None)))
        self.assertTrue(callable(getattr(s.NesterovAcceleratedGradient,"__init__",None)))
        self.assertTrue(callable(getattr(s.NesterovAcceleratedGradient,"update",None)))
        self.assertTrue(callable(getattr(s.Adagrad,"__init__",None)))
        self.assertTrue(callable(getattr(s.Adagrad,"update",None)))
        self.assertTrue(callable(getattr(s.Adadelta,"__init__",None)))
        self.assertTrue(callable(getattr(s.Adadelta,"update",None)))
        self.assertTrue(callable(getattr(s.RMSprop,"__init__",None)))
        self.assertTrue(callable(getattr(s.RMSprop,"update",None)))
        self.assertTrue(callable(getattr(s.Adam,"__init__",None)))
        self.assertTrue(callable(getattr(s.Adam,"update",None)))

    def test_sgd_decreases_norm(self):
        m=s.StochasticGradientDescent(learning_rate=.1)
        w=np.array([1.,-1.]);w2=np.asarray(m.update(w,w*2))
        self.assertLess(float(w2@w2),float(w@w))
    def test_adam_shape(self):
        m=s.Adam(learning_rate=.01)
        w=np.array([2.,-3.]);updated=np.asarray(m.update(w,2*w))
        self.assertEqual(updated.shape,w.shape)
