"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.RBM,"__init__",None)))
        self.assertTrue(callable(getattr(s.RBM,"fit",None)))
        self.assertTrue(callable(getattr(s.RBM,"reconstruct",None)))

    def test_reconstruction_shape(self):
        np.random.seed(0)
        X=np.array([[0.,1.,0.],[1.,0.,1.],[1.,1.,0.]])
        m=s.RBM(n_hidden=2,n_iterations=5,batch_size=2)
        m.fit(X)
        self.assertEqual(np.asarray(m.reconstruct(X)).shape,X.shape)
