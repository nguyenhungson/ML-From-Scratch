# Logistic Regression

**Module ID:** `supervised_learning/logistic_regression`  
**Mức độ:** 02 Supervised  
**Mục tiêu:** Huấn luyện bộ phân loại nhị phân bằng gradient descent.

## 1. Kiến thức toán học cần hiểu

p=σ(Xw+b), σ(z)=1/(1+e^(−z)); ∇w=Xᵀ(p−y)/n; BCE=−mean[y log p+(1−y) log(1−p)].

## 2. Đầu vào / đầu ra

fit(X,y,n_iterations); predict(X) -> nhãn 0/1.

## 3. Từng bước tự implement

1. **Bước 1:** Triển khai sigmoid ổn định số học.
2. **Bước 2:** Khởi tạo weights và bias (hoặc thêm cột 1).
3. **Bước 3:** Tính gradient BCE và cập nhật theo learning_rate.
4. **Bước 4:** Predict trả nhãn 0/1 theo threshold 0.5.
5. **Bước 5:** Kiểm tra loss giảm và có thể học dữ liệu linearly separable.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/logistic_regression.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `LogisticRegression.__init__(self, learning_rate=0.1, gradient_descent=True)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `LogisticRegression._initialize_parameters(self, X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `LogisticRegression.fit(self, X, y, n_iterations=4000)`: Ước lượng tham số từ tập huấn luyện.
- `LogisticRegression.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/logistic_regression
python practice/run.py test supervised_learning/logistic_regression
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Tách hai cụm dễ để accuracy > 0.9.

## 7. Cạm bẫy thường gặp

Cần bias/intercept; tránh tràn exp; scale features nếu cần.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/logistic_regression.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
