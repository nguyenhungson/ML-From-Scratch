"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s,"shuffle_data",None)))
        self.assertTrue(callable(getattr(s,"batch_iterator",None)))
        self.assertTrue(callable(getattr(s,"divide_on_feature",None)))
        self.assertTrue(callable(getattr(s,"polynomial_features",None)))
        self.assertTrue(callable(getattr(s,"get_random_subsets",None)))
        self.assertTrue(callable(getattr(s,"normalize",None)))
        self.assertTrue(callable(getattr(s,"standardize",None)))
        self.assertTrue(callable(getattr(s,"train_test_split",None)))
        self.assertTrue(callable(getattr(s,"k_fold_cross_validation_sets",None)))
        self.assertTrue(callable(getattr(s,"to_categorical",None)))
        self.assertTrue(callable(getattr(s,"to_nominal",None)))
        self.assertTrue(callable(getattr(s,"make_diagonal",None)))

    def test_split(self):
        X=np.arange(20).reshape(10,2);y=np.arange(10)
        Xtr,Xte,ytr,yte=s.train_test_split(X,y,test_size=0.2,shuffle=False)
        self.assertEqual(len(Xtr),8);self.assertEqual(len(Xte),2)
        np.testing.assert_array_equal(ytr,np.arange(8))
    def test_onehot(self):
        A=s.to_categorical(np.array([2,0,1]),n_col=3)
        np.testing.assert_array_equal(A,np.array([[0,0,1],[1,0,0],[0,1,0]]))
