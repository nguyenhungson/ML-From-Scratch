# Gaussian Mixture Model (EM)

**Module ID:** `unsupervised_learning/gaussian_mixture_model`  
**Mức độ:** 04 Unsupervised  
**Mục tiêu:** Tìm mô hình hỗn hợp Gaussian bằng Expectation-Maximization.

## 1. Kiến thức toán học cần hiểu

γ_ik=π_k N(x_i|μ_k,Σ_k)/Σ_jπ_j N(x_i|μ_j,Σ_j); μ_k=Σ_iγ_ikx_i/Σ_iγ_ik.

## 2. Đầu vào / đầu ra

predict(X)->(n,) cluster id (fit tự trong predict theo API gốc).

## 3. Từng bước tự implement

1. **Bước 1:** Khởi tạo mixture weights/means/covariances.
2. **Bước 2:** E-step responsibilities ổn định qua logsumexp.
3. **Bước 3:** M-step update π, μ, Σ.
4. **Bước 4:** Kiểm tra log-likelihood monotonic và stopping criterion.
5. **Bước 5:** Trả component assignment bằng argmax responsibilities.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/unsupervised_learning/gaussian_mixture_model.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `GaussianMixtureModel.__init__(self, k=2, max_iterations=2000, tolerance=1e-08)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `GaussianMixtureModel._init_random_gaussians(self, X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `GaussianMixtureModel.multivariate_gaussian(self, X, params)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `GaussianMixtureModel._get_likelihoods(self, X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `GaussianMixtureModel._expectation(self, X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `GaussianMixtureModel._maximization(self, X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `GaussianMixtureModel._converged(self, X)`: Kiểm tra điều kiện dừng.
- `GaussianMixtureModel.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show unsupervised_learning/gaussian_mixture_model
python practice/run.py test unsupervised_learning/gaussian_mixture_model
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Hai cụm Gaussian tách xa được gán khác component.

## 7. Cạm bẫy thường gặp

Cộng diagonal jitter tránh singular covariance; cluster labels tùy hoán vị.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/unsupervised_learning/gaussian_mixture_model.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
