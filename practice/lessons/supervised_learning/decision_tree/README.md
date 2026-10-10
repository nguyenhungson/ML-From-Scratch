# Decision Tree classification/regression

**Module ID:** `supervised_learning/decision_tree`  
**Mức độ:** 03 Supervised  
**Mục tiêu:** Xây dựng cây đệ quy bằng split giảm impurity.

## 1. Kiến thức toán học cần hiểu

Classification: Gini=1−Σp_c²; IG=H(parent)−Σ(n_child/n)H(child); Regression: giảm phương sai.

## 2. Đầu vào / đầu ra

fit(X,y), predict(X) -> (n,).

## 3. Từng bước tự implement

1. **Bước 1:** Thiết kế DecisionNode lưu feature, threshold, children hoặc leaf value.
2. **Bước 2:** Duyệt candidates split với min_samples_split/min_gain/max_depth.
3. **Bước 3:** Định nghĩa stopping conditions.
4. **Bước 4:** Dự đoán bằng cách traverse cây từ root tới leaf.
5. **Bước 5:** Kiểm tra cây không sinh nhánh rỗng.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/decision_tree.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `DecisionNode.__init__(self, feature_i=None, threshold=None, value=None, true_branch=None, false_branch=None)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `DecisionTree.__init__(self, min_samples_split=2, min_impurity=1e-07, max_depth=float('inf'), loss=None)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `DecisionTree.fit(self, X, y, loss=None)`: Ước lượng tham số từ tập huấn luyện.
- `DecisionTree._build_tree(self, X, y, current_depth=0)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `DecisionTree.predict_value(self, x, tree=None)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `DecisionTree.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.
- `DecisionTree.print_tree(self, tree=None, indent=' ')`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `XGBoostRegressionTree._split(self, y)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `XGBoostRegressionTree._gain(self, y, y_pred)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `XGBoostRegressionTree._gain_by_taylor(self, y, y1, y2)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `XGBoostRegressionTree._approximate_update(self, y)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `XGBoostRegressionTree.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `RegressionTree._calculate_variance_reduction(self, y, y1, y2)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `RegressionTree._mean_of_y(self, y)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `RegressionTree.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `ClassificationTree._calculate_information_gain(self, y, y1, y2)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `ClassificationTree._majority_vote(self, y)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `ClassificationTree.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/decision_tree
python practice/run.py test supervised_learning/decision_tree
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Cây độ sâu vừa phải giải được bài OR/AND, tree regression trả mean ở leaf.

## 7. Cạm bẫy thường gặp

Split numeric vs categorical khác nhau; kiểm tra feature và threshold hợp lệ.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/decision_tree.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
