"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.KNN,"__init__",None)))
        self.assertTrue(callable(getattr(s.KNN,"predict",None)))

    def test_k1(self):
        X=np.array([[0.,0.],[10.,10.],[0.,1.],[10.,11.]])
        y=np.array([0,1,0,1]);model=s.KNN(k=1)
        pred=model.predict(np.array([[.1,.1],[9.9,10.1]]),X,y)
        np.testing.assert_array_equal(pred,[0,1])
