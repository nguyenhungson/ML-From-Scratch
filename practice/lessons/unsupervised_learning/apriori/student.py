"""BÀI THỰC HÀNH ĐỘC LẬP - unsupervised_learning/apriori
Không import từ mlfromscratch hoặc bất kỳ lesson nào khác.
Chỉ dùng NumPy/standard library, trừ trường hợp cần vẽ và đã ghi trong README.
Giữ nguyên signature; tự cài đặt từng hàm/method, xóa NotImplementedError.
"""
from __future__ import annotations

import math
import numpy as np

class Rule:
    """Hoàn thiện class Rule từ đầu."""
    def __init__(self, antecedent, concequent, confidence, support):
        pass


class Apriori:
    """Hoàn thiện class Apriori từ đầu."""
    def __init__(self, min_sup=0.3, min_conf=0.81):
        pass

    def _calculate_support(self, itemset):
        pass

    def _get_frequent_itemsets(self, candidates):
        pass

    def _has_infrequent_itemsets(self, candidate):
        pass

    def _generate_candidates(self, freq_itemset):
        pass

    def _transaction_contains_items(self, transaction, items):
        pass

    def find_frequent_itemsets(self, transactions):
        pass

    def _rules_from_itemset(self, initial_itemset, itemset):
        pass

    def generate_rules(self, transactions):
        pass
