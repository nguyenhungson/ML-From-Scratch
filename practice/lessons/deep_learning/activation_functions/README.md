# Activation Functions

**Module ID:** `deep_learning/activation_functions`  
**Mức độ:** 02 Deep Learning  
**Mục tiêu:** Viết activation và đạo hàm để dùng cho backprop.

## 1. Kiến thức toán học cần hiểu

σ(x)=1/(1+e^-x), σ′=σ(1−σ); ReLU=max(0,x); tanh′=1−tanh²(x); softmax(x)_i=e^(x_i−max x)/Σ_j e^(x_j−max x).

## 2. Đầu vào / đầu ra

__call__(x)->same shape; gradient(x)->same shape (Softmax Jacobian cần chỉ rõ quy ước).

## 3. Từng bước tự implement

1. **Bước 1:** Cài đặt sigmoid, tanh, relu, leaky relu.
2. **Bước 2:** Cài đặt softmax ổn định trên trục class.
3. **Bước 3:** Viết đạo hàm theo quy ước gradient(x) của repo.
4. **Bước 4:** Thử finite differences cho các đạo hàm pointwise.
5. **Bước 5:** Bổ sung ELU, SELU, SoftPlus.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/deep_learning/activation_functions.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `Sigmoid.__call__(self, x)`: Thực thi phép biến đổi/toán tử trên đầu vào.
- `Sigmoid.gradient(self, x)`: Trả gradient theo định nghĩa của hàm loss/activation.
- `Softmax.__call__(self, x)`: Thực thi phép biến đổi/toán tử trên đầu vào.
- `Softmax.gradient(self, x)`: Trả gradient theo định nghĩa của hàm loss/activation.
- `TanH.__call__(self, x)`: Thực thi phép biến đổi/toán tử trên đầu vào.
- `TanH.gradient(self, x)`: Trả gradient theo định nghĩa của hàm loss/activation.
- `ReLU.__call__(self, x)`: Thực thi phép biến đổi/toán tử trên đầu vào.
- `ReLU.gradient(self, x)`: Trả gradient theo định nghĩa của hàm loss/activation.
- `LeakyReLU.__init__(self, alpha=0.2)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `LeakyReLU.__call__(self, x)`: Thực thi phép biến đổi/toán tử trên đầu vào.
- `LeakyReLU.gradient(self, x)`: Trả gradient theo định nghĩa của hàm loss/activation.
- `ELU.__init__(self, alpha=0.1)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `ELU.__call__(self, x)`: Thực thi phép biến đổi/toán tử trên đầu vào.
- `ELU.gradient(self, x)`: Trả gradient theo định nghĩa của hàm loss/activation.
- `SELU.__init__(self)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `SELU.__call__(self, x)`: Thực thi phép biến đổi/toán tử trên đầu vào.
- `SELU.gradient(self, x)`: Trả gradient theo định nghĩa của hàm loss/activation.
- `SoftPlus.__call__(self, x)`: Thực thi phép biến đổi/toán tử trên đầu vào.
- `SoftPlus.gradient(self, x)`: Trả gradient theo định nghĩa của hàm loss/activation.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show deep_learning/activation_functions
python practice/run.py test deep_learning/activation_functions
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

σ(0)=0.5, ReLU(-1)=0, softmax mỗi row tổng=1.

## 7. Cạm bẫy thường gặp

Đạo hàm softmax là Jacobian; không nhầm với đạo hàm elementwise của sigmoid.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/deep_learning/activation_functions.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
