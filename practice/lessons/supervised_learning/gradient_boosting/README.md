# Gradient Boosting

**Module ID:** `supervised_learning/gradient_boosting`  
**Mức độ:** 04 Ensemble  
**Mục tiêu:** Giảm loss bằng việc tuần tự fit cây vào negative gradients.

## 1. Kiến thức toán học cần hiểu

F_m(x)=F_{m−1}(x)+η h_m(x); square loss pseudo-residual r_i=y_i−F_{m−1}(x_i).

## 2. Đầu vào / đầu ra

fit(X,y), predict(X)->(n,).

## 3. Từng bước tự implement

1. **Bước 1:** Khởi tạo prediction theo mean target hoặc logits.
2. **Bước 2:** Tính pseudo residuals/negative gradient.
3. **Bước 3:** Fit regression tree mới lên residuals.
4. **Bước 4:** Update bằng learning_rate.
5. **Bước 5:** Phân loại: liên hệ logistic link và probability.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/gradient_boosting.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `GradientBoosting.__init__(self, n_estimators, learning_rate, min_samples_split, min_impurity, max_depth, regression)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `GradientBoosting.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `GradientBoosting.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.
- `GradientBoostingRegressor.__init__(self, n_estimators=200, learning_rate=0.5, min_samples_split=2, min_var_red=1e-07, max_depth=4, debug=False)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `GradientBoostingClassifier.__init__(self, n_estimators=200, learning_rate=0.5, min_samples_split=2, min_info_gain=1e-07, max_depth=2, debug=False)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `GradientBoostingClassifier.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/gradient_boosting
python practice/run.py test supervised_learning/gradient_boosting
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Hồi quy y=x² trên dữ liệu nhỏ; MSE giảm theo số estimators.

## 7. Cạm bẫy thường gặp

Không fit tất cả cây cùng y vì sẽ thành bagging, không phải boosting.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/gradient_boosting.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
