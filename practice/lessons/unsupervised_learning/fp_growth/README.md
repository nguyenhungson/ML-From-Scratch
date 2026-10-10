# FP-Growth

**Module ID:** `unsupervised_learning/fp_growth`  
**Mức độ:** 05 Data mining  
**Mục tiêu:** Khai phá frequent itemsets mà không enumerate toàn bộ candidates như Apriori.

## 1. Kiến thức toán học cần hiểu

Support của itemset bằng tổng đếm các đường điều kiện trong FP-tree.

## 2. Đầu vào / đầu ra

find_frequent_itemsets(transactions, suffix=None, show_tree=False).

## 3. Từng bước tự implement

1. **Bước 1:** Đếm frequent singleton, sắp thứ tự theo frequency.
2. **Bước 2:** Thiết kế FP-tree node và header table.
3. **Bước 3:** Chèn sorted transactions.
4. **Bước 4:** Tìm conditional pattern bases và conditional FP-trees.
5. **Bước 5:** Phát sinh frequent itemsets recursively.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/unsupervised_learning/fp_growth.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `FPTreeNode.__init__(self, item=None, support=1)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `FPGrowth.__init__(self, min_sup=0.3)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `FPGrowth._calculate_support(self, item, transactions)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `FPGrowth._get_frequent_items(self, transactions)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `FPGrowth._insert_tree(self, node, children)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `FPGrowth._construct_tree(self, transactions, frequent_items=None)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `FPGrowth.print_tree(self, node=None, indent_times=0)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `FPGrowth._is_prefix(self, itemset, node)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `FPGrowth._determine_prefixes(self, itemset, node, prefixes=None)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `FPGrowth._get_itemset_key(self, itemset)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `FPGrowth._determine_frequent_itemsets(self, conditional_database, suffix)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `FPGrowth.find_frequent_itemsets(self, transactions, suffix=None, show_tree=False)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show unsupervised_learning/fp_growth
python practice/run.py test unsupervised_learning/fp_growth
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Trên dataset basket nhỏ trả itemsets có support đúng.

## 7. Cạm bẫy thường gặp

Quan trọng giữ node count và links; frequent itemsets được biểu diễn không trùng.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/unsupervised_learning/fp_growth.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
