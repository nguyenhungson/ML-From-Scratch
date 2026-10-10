"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.KMeans,"__init__",None)))
        self.assertTrue(callable(getattr(s.KMeans,"predict",None)))

    def test_two_clusters(self):
        np.random.seed(0)
        X=np.array([[0.,0.],[0.,.2],[.1,0.],[10.,10.],[10.,10.2],[10.2,10.]])
        labels=np.asarray(s.KMeans(k=2,max_iterations=100).predict(X)).ravel()
        self.assertEqual(labels.shape,(6,))
        self.assertEqual(len(set(labels[:3])),1)
        self.assertEqual(len(set(labels[3:])),1)
        self.assertNotEqual(labels[0],labels[3])
