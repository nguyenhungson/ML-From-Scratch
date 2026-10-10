# Perceptron classifier

**Module ID:** `supervised_learning/perceptron`  
**Mức độ:** 02 Supervised  
**Mục tiêu:** Tự hiện thực phân loại tuyến tính từ dữ liệu có nhãn.

## 1. Kiến thức toán học cần hiểu

ŷ=sign(wᵀx+b); cập nhật khi nhãn sai: w←w+η yx, b←b+ηy (y ∈ {−1,+1}).

## 2. Đầu vào / đầu ra

fit(X:(n,d), y:(n,)); predict(X)->(n,) với nhãn như đầu vào.

## 3. Từng bước tự implement

1. **Bước 1:** Kiểm tra y thuộc {-1,+1} hoặc mã hóa từ {0,1}.
2. **Bước 2:** Khởi tạo weights, bias.
3. **Bước 3:** Duyệt epochs và cập nhật theo từng mẫu bị phân loại sai.
4. **Bước 4:** Viết predict và kiểm tra dữ liệu linearly separable.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/perceptron.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `Perceptron.__init__(self, n_iterations=20000, activation_function=None, loss=None, learning_rate=0.01)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Perceptron.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `Perceptron.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/perceptron
python practice/run.py test supervised_learning/perceptron
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

AND logic hoặc 2 cụm phân tách tuyến tính.

## 7. Cạm bẫy thường gặp

Nếu giữ nguyên chữ ký gốc có activation_function/loss, tự quyết định cách vận dụng và ghi vào README cá nhân.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/perceptron.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
