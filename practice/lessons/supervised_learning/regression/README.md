# Hồi quy tuyến tính và regularization

**Module ID:** `supervised_learning/regression`  
**Mức độ:** 03 Supervised  
**Mục tiêu:** Tự viết Linear, Ridge, Lasso, Elastic Net và polynomial features.

## 1. Kiến thức toán học cần hiểu

MSE=mean((Xw−y)²); Ridge: MSE+λ||w||²₂; Lasso: MSE+λ||w||₁; Elastic Net: L1+L2.

## 2. Đầu vào / đầu ra

X: (n,d), y:(n,) hoặc (n,1); predict(X) -> (n,) / (n,1).

## 3. Từng bước tự implement

1. **Bước 1:** Viết Regression base cùng intercept.
2. **Bước 2:** LinearRegression: nghiệm least-squares hoặc gradient descent.
3. **Bước 3:** Ridge L2 gradient, Lasso dùng subgradient hoặc coordinate descent.
4. **Bước 4:** Polynomial feature expansion rồi fit regression.
5. **Bước 5:** So sánh train error, regularization, overfit.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/regression.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `l1_regularization.__init__(self, alpha)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `l1_regularization.__call__(self, w)`: Thực thi phép biến đổi/toán tử trên đầu vào.
- `l1_regularization.grad(self, w)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `l2_regularization.__init__(self, alpha)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `l2_regularization.__call__(self, w)`: Thực thi phép biến đổi/toán tử trên đầu vào.
- `l2_regularization.grad(self, w)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `l1_l2_regularization.__init__(self, alpha, l1_ratio=0.5)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `l1_l2_regularization.__call__(self, w)`: Thực thi phép biến đổi/toán tử trên đầu vào.
- `l1_l2_regularization.grad(self, w)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Regression.__init__(self, n_iterations, learning_rate)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Regression.initialize_weights(self, n_features)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Regression.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `Regression.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.
- `LinearRegression.__init__(self, n_iterations=100, learning_rate=0.001, gradient_descent=True)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `LinearRegression.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `LassoRegression.__init__(self, degree, reg_factor, n_iterations=3000, learning_rate=0.01)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `LassoRegression.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `LassoRegression.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.
- `PolynomialRegression.__init__(self, degree, n_iterations=3000, learning_rate=0.001)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `PolynomialRegression.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `PolynomialRegression.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.
- `RidgeRegression.__init__(self, reg_factor, n_iterations=1000, learning_rate=0.001)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `PolynomialRidgeRegression.__init__(self, degree, reg_factor, n_iterations=3000, learning_rate=0.01, gradient_descent=True)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `PolynomialRidgeRegression.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `PolynomialRidgeRegression.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.
- `ElasticNet.__init__(self, degree=1, reg_factor=0.05, l1_ratio=0.5, n_iterations=3000, learning_rate=0.01)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `ElasticNet.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `ElasticNet.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/regression
python practice/run.py test supervised_learning/regression
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Với y=2x+1, dự đoán sát kết quả; weight shrinkage tăng khi lambda tăng.

## 7. Cạm bẫy thường gặp

Không regularize intercept; nhất quán shape vector và matrix.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/regression.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
