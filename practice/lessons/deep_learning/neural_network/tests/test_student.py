"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.NeuralNetwork,"__init__",None)))
        self.assertTrue(callable(getattr(s.NeuralNetwork,"set_trainable",None)))
        self.assertTrue(callable(getattr(s.NeuralNetwork,"add",None)))
        self.assertTrue(callable(getattr(s.NeuralNetwork,"test_on_batch",None)))
        self.assertTrue(callable(getattr(s.NeuralNetwork,"train_on_batch",None)))
        self.assertTrue(callable(getattr(s.NeuralNetwork,"fit",None)))
        self.assertTrue(callable(getattr(s.NeuralNetwork,"summary",None)))
        self.assertTrue(callable(getattr(s.NeuralNetwork,"predict",None)))
    def test_constructor_is_implemented(self):
        # First milestone of advanced lesson: initialize a clean state without external repository imports.
        model=s.NeuralNetwork(None, None)
        self.assertIsNotNone(model)
