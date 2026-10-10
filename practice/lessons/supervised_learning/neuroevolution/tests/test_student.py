"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.Neuroevolution,"__init__",None)))
        self.assertTrue(callable(getattr(s.Neuroevolution,"evolve",None)))
    def test_constructor_is_implemented(self):
        # First milestone of advanced lesson: initialize a clean state without external repository imports.
        model=s.Neuroevolution(None, None, None)
        self.assertIsNotNone(model)
