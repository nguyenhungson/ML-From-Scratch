"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.MultilayerPerceptron,"__init__",None)))
        self.assertTrue(callable(getattr(s.MultilayerPerceptron,"fit",None)))
        self.assertTrue(callable(getattr(s.MultilayerPerceptron,"predict",None)))
        self.assertTrue(callable(getattr(s,"main",None)))

    def test_shapes(self):
        X=np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
        y=np.array([0,1,1,0]);m=s.MultilayerPerceptron(n_hidden=5,n_iterations=500,learning_rate=0.1)
        m.fit(X,y);pred=np.asarray(m.predict(X))
        self.assertEqual(len(pred),4)
