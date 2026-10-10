# Apriori frequent itemsets

**Module ID:** `unsupervised_learning/apriori`  
**Mức độ:** 04 Data mining  
**Mục tiêu:** Khai phá tập mục phổ biến và association rules.

## 1. Kiến thức toán học cần hiểu

support(A)=count(tx chứa A)/N; confidence(A⇒B)=support(A∪B)/support(A).

## 2. Đầu vào / đầu ra

find_frequent_itemsets(transactions); generate_rules(transactions).

## 3. Từng bước tự implement

1. **Bước 1:** Đếm 1-item frequent sets.
2. **Bước 2:** Sinh candidate k từ frequent (k−1) và prune các subset không frequent.
3. **Bước 3:** Tính support ở transaction level.
4. **Bước 4:** Sinh luật A⇒B từ frequent sets.
5. **Bước 5:** Lọc theo min_conf.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/unsupervised_learning/apriori.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `Rule.__init__(self, antecedent, concequent, confidence, support)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Apriori.__init__(self, min_sup=0.3, min_conf=0.81)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Apriori._calculate_support(self, itemset)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Apriori._get_frequent_itemsets(self, candidates)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Apriori._has_infrequent_itemsets(self, candidate)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Apriori._generate_candidates(self, freq_itemset)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Apriori._transaction_contains_items(self, transaction, items)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Apriori.find_frequent_itemsets(self, transactions)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Apriori._rules_from_itemset(self, initial_itemset, itemset)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Apriori.generate_rules(self, transactions)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show unsupervised_learning/apriori
python practice/run.py test unsupervised_learning/apriori
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Basket [A,B],[A],[A,B,C] với min_sup=2/3 trả A, B và {A,B}.

## 7. Cạm bẫy thường gặp

Dùng frozenset làm khóa để set operations nhất quán.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/unsupervised_learning/apriori.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
