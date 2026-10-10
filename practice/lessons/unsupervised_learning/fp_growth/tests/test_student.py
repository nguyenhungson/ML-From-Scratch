"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.FPTreeNode,"__init__",None)))
        self.assertTrue(callable(getattr(s.FPGrowth,"__init__",None)))
        self.assertTrue(callable(getattr(s.FPGrowth,"print_tree",None)))
        self.assertTrue(callable(getattr(s.FPGrowth,"find_frequent_itemsets",None)))

    def test_itemsets(self):
        tx=[['A','B'],['A'],['A','B','C']]
        result=s.FPGrowth(min_sup=2/3).find_frequent_itemsets(tx)
        self.assertIsNotNone(result)
        self.assertGreater(len(result),0)
