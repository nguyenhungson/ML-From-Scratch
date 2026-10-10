"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.DecisionNode,"__init__",None)))
        self.assertTrue(callable(getattr(s.DecisionTree,"__init__",None)))
        self.assertTrue(callable(getattr(s.DecisionTree,"fit",None)))
        self.assertTrue(callable(getattr(s.DecisionTree,"predict_value",None)))
        self.assertTrue(callable(getattr(s.DecisionTree,"predict",None)))
        self.assertTrue(callable(getattr(s.DecisionTree,"print_tree",None)))
        self.assertTrue(callable(getattr(s.XGBoostRegressionTree,"fit",None)))
        self.assertTrue(callable(getattr(s.RegressionTree,"fit",None)))
        self.assertTrue(callable(getattr(s.ClassificationTree,"fit",None)))

    def test_classification_tree(self):
        X=np.array([[0.],[1.],[2.],[3.]])
        y=np.array([0,0,1,1]);m=s.ClassificationTree(max_depth=3)
        m.fit(X,y)
        np.testing.assert_array_equal(np.asarray(m.predict(X)).ravel(),y)
