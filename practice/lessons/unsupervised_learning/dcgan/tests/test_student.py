"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.DCGAN,"__init__",None)))
        self.assertTrue(callable(getattr(s.DCGAN,"build_generator",None)))
        self.assertTrue(callable(getattr(s.DCGAN,"build_discriminator",None)))
        self.assertTrue(callable(getattr(s.DCGAN,"train",None)))
        self.assertTrue(callable(getattr(s.DCGAN,"save_imgs",None)))
    def test_constructor_is_implemented(self):
        # First milestone of advanced lesson: initialize a clean state without external repository imports.
        model=s.DCGAN()
        self.assertIsNotNone(model)
