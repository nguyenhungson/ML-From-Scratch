"""Bài kiểm thử riêng cho lesson: chạy bằng practice/run.py test <id>."""
import pathlib
import sys
import unittest
import numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import student as s

class TestLesson(unittest.TestCase):
    def test_public_api(self):
        self.assertTrue(callable(getattr(s.Rule,"__init__",None)))
        self.assertTrue(callable(getattr(s.Apriori,"__init__",None)))
        self.assertTrue(callable(getattr(s.Apriori,"find_frequent_itemsets",None)))
        self.assertTrue(callable(getattr(s.Apriori,"generate_rules",None)))

    def test_retrieve_itemsets(self):
        tx=[['A','B'],['A'],['A','B','C']]
        itemsets=s.Apriori(min_sup=2/3).find_frequent_itemsets(tx)
        self.assertIsNotNone(itemsets)
        self.assertGreater(len(itemsets),0)
