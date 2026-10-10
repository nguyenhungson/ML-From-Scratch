"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.DBSCAN,"__init__",None)))
        self.assertTrue(callable(getattr(s.DBSCAN,"predict",None)))

    def test_noise(self):
        X=np.array([[0.,0.],[0.,.1],[.1,0.],[5.,5.],[5.,5.1],[5.1,5.],[20.,20.]])
        labels=np.asarray(s.DBSCAN(eps=.3,min_samples=3).predict(X)).ravel()
        self.assertEqual(labels.shape,(7,))
        self.assertEqual(labels[-1],-1)
        self.assertEqual(len(set(labels[:3])),1)
        self.assertNotEqual(labels[0],labels[3])
