# Bayesian Linear Regression

**Module ID:** `supervised_learning/bayesian_regression`  
**Mức độ:** 05 Xác suất  
**Mục tiêu:** Ước lượng phân phối hậu nghiệm trên hệ số hồi quy thay vì một điểm dự đoán.

## 1. Kiến thức toán học cần hiểu

posterior precision Λ_n=Λ_0+βXᵀX; posterior mean μ_n=Λ_n⁻¹(Λ_0μ_0+βXᵀy).

## 2. Đầu vào / đầu ra

fit(X,y) rồi predict(X,eti=False); output theo lựa chọn rõ ràng.

## 3. Từng bước tự implement

1. **Bước 1:** Xác định prior trên weights/noise variance.
2. **Bước 2:** Tính posterior từ conjugate prior.
3. **Bước 3:** Lấy posterior predictive mean.
4. **Bước 4:** Lấy posterior draws và credible intervals.
5. **Bước 5:** Kiểm tra độ rộng interval giảm khi có thêm dữ liệu.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/bayesian_regression.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `BayesianRegression.__init__(self, n_draws, mu0, omega0, nu0, sigma_sq0, poly_degree=0, cred_int=95)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `BayesianRegression._draw_scaled_inv_chi_sq(self, n, df, scale)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `BayesianRegression.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `BayesianRegression.predict(self, X, eti=False)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/bayesian_regression
python practice/run.py test supervised_learning/bayesian_regression
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Dữ liệu y=2x+1+noise; mean gần đường true.

## 7. Cạm bẫy thường gặp

Cần xác định chính xác prior hyperparameters, mức CI và shape samples.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/bayesian_regression.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
