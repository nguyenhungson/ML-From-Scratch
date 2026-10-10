# Neural Network training engine

**Module ID:** `deep_learning/neural_network`  
**Mức độ:** 05 Deep Learning  
**Mục tiêu:** Lắp ghép layer, optimizer, loss và thực hiện backprop end-to-end.

## 1. Kiến thức toán học cần hiểu

forward: x→L₁→⋯→L_k→ŷ; backprop: ∂L/∂h_i=(∂L/∂h_{i+1})(∂h_{i+1}/∂h_i).

## 2. Đầu vào / đầu ra

NeuralNetwork(optimizer,loss); add(layer); fit(X,y,n_epochs,batch_size), predict(X).

## 3. Từng bước tự implement

1. **Bước 1:** Định nghĩa add() thêm layer, initialize shape.
2. **Bước 2:** Forward pass theo thứ tự.
3. **Bước 3:** Backward pass đảo chiều qua layers.
4. **Bước 4:** Viết mini-batch fit và predict.
5. **Bước 5:** So sánh train loss và gradient checks.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/deep_learning/neural_network.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `NeuralNetwork.__init__(self, optimizer, loss, validation_data=None)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `NeuralNetwork.set_trainable(self, trainable)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `NeuralNetwork.add(self, layer)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `NeuralNetwork.test_on_batch(self, X, y)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `NeuralNetwork.train_on_batch(self, X, y)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `NeuralNetwork.fit(self, X, y, n_epochs, batch_size)`: Ước lượng tham số từ tập huấn luyện.
- `NeuralNetwork._forward_pass(self, X, training=True)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `NeuralNetwork._backward_pass(self, loss_grad)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `NeuralNetwork.summary(self, name='Model Summary')`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `NeuralNetwork.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show deep_learning/neural_network
python practice/run.py test deep_learning/neural_network
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Học XOR hoặc regression nhỏ khi Dense/loss đã hoạt động.

## 7. Cạm bẫy thường gặp

Đây là bài tổng hợp; tập trung test từng layer độc lập trước.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/deep_learning/neural_network.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
