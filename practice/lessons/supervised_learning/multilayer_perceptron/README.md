# MLP từ đầu

**Module ID:** `supervised_learning/multilayer_perceptron`  
**Mức độ:** 05 Deep Learning  
**Mục tiêu:** Huấn luyện mạng fully-connected một hidden layer bằng backpropagation.

## 1. Kiến thức toán học cần hiểu

h=σ(XW₁+b₁); ŷ=softmax(hW₂+b₂); δ₂=ŷ−Y; δ₁=(δ₂W₂ᵀ)⊙σ′(z₁).

## 2. Đầu vào / đầu ra

fit(X,y), predict(X) -> (n,) hoặc class logits theo mô tả của bạn.

## 3. Từng bước tự implement

1. **Bước 1:** Khởi tạo W1,b1,W2,b2 đúng shape.
2. **Bước 2:** Forward: dense->activation->dense->softmax.
3. **Bước 3:** Tính cross-entropy, backprop gradients.
4. **Bước 4:** SGD update và lập train loop.
5. **Bước 5:** Predict nhãn class (argmax).

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/multilayer_perceptron.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `MultilayerPerceptron.__init__(self, n_hidden, n_iterations=3000, learning_rate=0.01)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `MultilayerPerceptron._initialize_weights(self, X, y)`: Tạo trọng số ban đầu với shape đúng.
- `MultilayerPerceptron.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `MultilayerPerceptron.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.
- `main()`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/multilayer_perceptron
python practice/run.py test supervised_learning/multilayer_perceptron
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

XOR 4 điểm với nhiều epochs/seed có thể học đạt accuracy cao.

## 7. Cạm bẫy thường gặp

Sai lệch nhãn one-hot và broadcasting rất dễ làm gradient sai.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/multilayer_perceptron.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
