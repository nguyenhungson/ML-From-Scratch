# XGBoost-style tree boosting

**Module ID:** `supervised_learning/xgboost`  
**Mức độ:** 06 Advanced  
**Mục tiêu:** Xây dựng boosting xấp xỉ Newton bước hai theo gradient và Hessian.

## 1. Kiến thức toán học cần hiểu

gain=½[G_L²/(H_L+λ)+G_R²/(H_R+λ)−G²/(H+λ)]−γ; leaf_value=−G/(H+λ).

## 2. Đầu vào / đầu ra

fit(X,y), predict(X) và test loss giảm trên toy set.

## 3. Từng bước tự implement

1. **Bước 1:** Viết logistic loss gradient và Hessian.
2. **Bước 2:** Tạo splits tính G,H.
3. **Bước 3:** Fit regression tree với leaf Newton weights.
4. **Bước 4:** Update score dùng learning rate.
5. **Bước 5:** Giải thích regularization lambda/gamma.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/xgboost.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `LogisticLoss.__init__(self)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `LogisticLoss.loss(self, y, y_pred)`: Tính loss tương ứng.
- `LogisticLoss.gradient(self, y, y_pred)`: Trả gradient theo định nghĩa của hàm loss/activation.
- `LogisticLoss.hess(self, y, y_pred)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `XGBoost.__init__(self, n_estimators=200, learning_rate=0.001, min_samples_split=2, min_impurity=1e-07, max_depth=2)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `XGBoost.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `XGBoost.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/xgboost
python practice/run.py test supervised_learning/xgboost
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Toy binary classification, predicted label hợp lý.

## 7. Cạm bẫy thường gặp

Đây là XGBoost-style educational code, không phải full XGBoost production.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/xgboost.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
