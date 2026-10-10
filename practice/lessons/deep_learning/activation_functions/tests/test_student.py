"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.Sigmoid,"gradient",None)))
        self.assertTrue(callable(getattr(s.Softmax,"gradient",None)))
        self.assertTrue(callable(getattr(s.TanH,"gradient",None)))
        self.assertTrue(callable(getattr(s.ReLU,"gradient",None)))
        self.assertTrue(callable(getattr(s.LeakyReLU,"__init__",None)))
        self.assertTrue(callable(getattr(s.LeakyReLU,"gradient",None)))
        self.assertTrue(callable(getattr(s.ELU,"__init__",None)))
        self.assertTrue(callable(getattr(s.ELU,"gradient",None)))
        self.assertTrue(callable(getattr(s.SELU,"__init__",None)))
        self.assertTrue(callable(getattr(s.SELU,"gradient",None)))
        self.assertTrue(callable(getattr(s.SoftPlus,"gradient",None)))

    def test_sigmoid(self):
        a=s.Sigmoid();np.testing.assert_allclose(a(np.array([-100.,0.,100.])),[0.,.5,1.],atol=1e-6)
        self.assertAlmostEqual(float(a.gradient(np.array([0.]))[0]),0.25)
    def test_relu_softmax(self):
        np.testing.assert_array_equal(s.ReLU()(np.array([-1.,0.,2.])),[0.,0.,2.])
        p=s.Softmax()(np.array([[1.,2.,3.],[3.,2.,1.]]))
        np.testing.assert_allclose(np.asarray(p).sum(axis=1),[1.,1.],atol=1e-8)
