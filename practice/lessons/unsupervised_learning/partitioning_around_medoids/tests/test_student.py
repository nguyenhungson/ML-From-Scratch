"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.PAM,"__init__",None)))
        self.assertTrue(callable(getattr(s.PAM,"predict",None)))

    def test_two_groups(self):
        np.random.seed(1)
        X=np.array([[0.,0.],[0.,1.],[1.,0.],[10.,10.],[10.,11.],[11.,10.]])
        label=np.asarray(s.PAM(k=2).predict(X)).ravel()
        self.assertEqual(label.shape,(6,))
        self.assertNotEqual(label[0],label[3])
