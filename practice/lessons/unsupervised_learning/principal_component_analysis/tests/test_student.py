"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.PCA,"transform",None)))

    def test_reduction(self):
        X=np.array([[1.,2.],[2.,4.],[3.,6.],[4.,8.]])
        Z=np.asarray(s.PCA().transform(X,n_components=1))
        self.assertEqual(Z.shape,(4,1))
        self.assertGreater(np.var(Z),0.)
