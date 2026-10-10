# Optimizers: SGD, Adam, RMSprop

**Module ID:** `deep_learning/optimizers`  
**Mức độ:** 03 Deep Learning  
**Mục tiêu:** Lập trình các optimizer dùng trong training loops.

## 1. Kiến thức toán học cần hiểu

SGD: w←w−ηg; momentum v←μv+g; Adam m←β₁m+(1−β₁)g, v←β₂v+(1−β₂)g².

## 2. Đầu vào / đầu ra

update(w,grad_wrt_w) -> updated ndarray.

## 3. Từng bước tự implement

1. **Bước 1:** Viết SGD và momentum.
2. **Bước 2:** Duy trì state per-parameter cho Adagrad, RMSprop.
3. **Bước 3:** Viết Adam với bias correction t và epsilon.
4. **Bước 4:** Kiểm tra shape và không mutate gradient.
5. **Bước 5:** Dùng hàm f(w)=.
6. **Bước 6:** .
7. **Bước 7:** w.
8. **Bước 8:** .
9. **Bước 9:** ² để test convergence.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/deep_learning/optimizers.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `StochasticGradientDescent.__init__(self, learning_rate=0.01, momentum=0)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `StochasticGradientDescent.update(self, w, grad_wrt_w)`: Cập nhật tham số tối ưu hóa.
- `NesterovAcceleratedGradient.__init__(self, learning_rate=0.001, momentum=0.4)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `NesterovAcceleratedGradient.update(self, w, grad_func)`: Cập nhật tham số tối ưu hóa.
- `Adagrad.__init__(self, learning_rate=0.01)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Adagrad.update(self, w, grad_wrt_w)`: Cập nhật tham số tối ưu hóa.
- `Adadelta.__init__(self, rho=0.95, eps=1e-06)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Adadelta.update(self, w, grad_wrt_w)`: Cập nhật tham số tối ưu hóa.
- `RMSprop.__init__(self, learning_rate=0.01, rho=0.9)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `RMSprop.update(self, w, grad_wrt_w)`: Cập nhật tham số tối ưu hóa.
- `Adam.__init__(self, learning_rate=0.001, b1=0.9, b2=0.999)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Adam.update(self, w, grad_wrt_w)`: Cập nhật tham số tối ưu hóa.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show deep_learning/optimizers
python practice/run.py test deep_learning/optimizers
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Với w=[1,-1] và g=2w, một bước SGD nhỏ giảm ||w||.

## 7. Cạm bẫy thường gặp

Adam dùng squared gradient second moment, không phải Hessian.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/deep_learning/optimizers.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
