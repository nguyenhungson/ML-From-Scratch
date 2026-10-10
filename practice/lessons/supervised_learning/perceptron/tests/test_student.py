"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.Perceptron,"__init__",None)))
        self.assertTrue(callable(getattr(s.Perceptron,"fit",None)))
        self.assertTrue(callable(getattr(s.Perceptron,"predict",None)))

    def test_api_on_toy_data(self):
        X=np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
        y=np.array([-1.,-1.,-1.,1.])
        m=s.Perceptron(n_iterations=2500,learning_rate=0.1)
        m.fit(X,y)
        pred=np.asarray(m.predict(X)).reshape(-1)
        self.assertEqual(pred.shape,y.shape)
        self.assertGreaterEqual(np.mean(pred==y),0.75)
