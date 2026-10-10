# Loss Functions

**Module ID:** `deep_learning/loss_functions`  
**Mức độ:** 02 Deep Learning  
**Mục tiêu:** Viết MSE và cross-entropy kèm gradients.

## 1. Kiến thức toán học cần hiểu

MSE=mean((y−ŷ)²); CE=−Σ y_c log p_c; derivative CE wrt probability = −y_c/p_c.

## 2. Đầu vào / đầu ra

loss(y_true,y_pred), gradient(y,y_pred), acc(y,y_pred).

## 3. Từng bước tự implement

1. **Bước 1:** Định nghĩa loss scalar/vector theo consistent reduction.
2. **Bước 2:** Viết gradients tương ứng đúng normalization.
3. **Bước 3:** Clip probabilities bằng eps.
4. **Bước 4:** Tính accuracy score với nhãn và one-hot.
5. **Bước 5:** Test bằng numerical finite difference.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/deep_learning/loss_functions.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `Loss.loss(self, y_true, y_pred)`: Tính loss tương ứng.
- `Loss.gradient(self, y, y_pred)`: Trả gradient theo định nghĩa của hàm loss/activation.
- `Loss.acc(self, y, y_pred)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `SquareLoss.__init__(self)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `SquareLoss.loss(self, y, y_pred)`: Tính loss tương ứng.
- `SquareLoss.gradient(self, y, y_pred)`: Trả gradient theo định nghĩa của hàm loss/activation.
- `CrossEntropy.__init__(self)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `CrossEntropy.loss(self, y, p)`: Tính loss tương ứng.
- `CrossEntropy.acc(self, y, p)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `CrossEntropy.gradient(self, y, p)`: Trả gradient theo định nghĩa của hàm loss/activation.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show deep_learning/loss_functions
python practice/run.py test deep_learning/loss_functions
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

MSE(y,y)=0; CE khi predicted đúng nhỏ hơn predicted sai.

## 7. Cạm bẫy thường gặp

Gradient phụ thuộc việc gọi trên probabilities hay logits; nhất quán.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/deep_learning/loss_functions.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
