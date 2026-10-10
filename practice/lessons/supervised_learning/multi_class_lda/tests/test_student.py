"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.MultiClassLDA,"__init__",None)))
        self.assertTrue(callable(getattr(s.MultiClassLDA,"transform",None)))
        self.assertTrue(callable(getattr(s.MultiClassLDA,"plot_in_2d",None)))

    def test_components(self):
        rng=np.random.RandomState(4)
        X=np.vstack([rng.normal(loc=i*4,size=(10,3)) for i in range(3)])
        y=np.repeat([0,1,2],10)
        Z=np.asarray(s.MultiClassLDA().transform(X,y,n_components=2))
        self.assertEqual(Z.shape,(30,2))
