# Neural Network Layers

**Module ID:** `deep_learning/layers`  
**Mức độ:** 04 Deep Learning  
**Mục tiêu:** Tự hiện thực forward/backward cho Dense, Flatten, Dropout, Conv2D, Pooling, RNN,...

## 1. Kiến thức toán học cần hiểu

Dense: Y=XW+b; dW=Xᵀ dY; dX=dY Wᵀ. Conv: correlation patches với kernels.

## 2. Đầu vào / đầu ra

forward_pass(X, training=True), backward_pass(accum_grad), output_shape().

## 3. Từng bước tự implement

1. **Bước 1:** Bắt đầu Layer interface (initialize, forward_pass, backward_pass).
2. **Bước 2:** Làm Dense, Flatten, Reshape và kiểm chứng gradients.
3. **Bước 3:** Làm Dropout & BatchNorm với train/inference modes.
4. **Bước 4:** Tiếp tục Conv2D, Pooling và padding.
5. **Bước 5:** Cuối cùng RNN/BPTT truncation.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/deep_learning/layers.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `Layer.set_input_shape(self, shape)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Layer.layer_name(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Layer.parameters(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Layer.forward_pass(self, X, training)`: Forward của layer / phép tính đầu ra.
- `Layer.backward_pass(self, accum_grad)`: Lan truyền gradient về lớp trước.
- `Layer.output_shape(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Dense.__init__(self, n_units, input_shape=None)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Dense.initialize(self, optimizer)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Dense.parameters(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Dense.forward_pass(self, X, training=True)`: Forward của layer / phép tính đầu ra.
- `Dense.backward_pass(self, accum_grad)`: Lan truyền gradient về lớp trước.
- `Dense.output_shape(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `RNN.__init__(self, n_units, activation='tanh', bptt_trunc=5, input_shape=None)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `RNN.initialize(self, optimizer)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `RNN.parameters(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `RNN.forward_pass(self, X, training=True)`: Forward của layer / phép tính đầu ra.
- `RNN.backward_pass(self, accum_grad)`: Lan truyền gradient về lớp trước.
- `RNN.output_shape(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Conv2D.__init__(self, n_filters, filter_shape, input_shape=None, padding='same', stride=1)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Conv2D.initialize(self, optimizer)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Conv2D.parameters(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Conv2D.forward_pass(self, X, training=True)`: Forward của layer / phép tính đầu ra.
- `Conv2D.backward_pass(self, accum_grad)`: Lan truyền gradient về lớp trước.
- `Conv2D.output_shape(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `BatchNormalization.__init__(self, momentum=0.99)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `BatchNormalization.initialize(self, optimizer)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `BatchNormalization.parameters(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `BatchNormalization.forward_pass(self, X, training=True)`: Forward của layer / phép tính đầu ra.
- `BatchNormalization.backward_pass(self, accum_grad)`: Lan truyền gradient về lớp trước.
- `BatchNormalization.output_shape(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `PoolingLayer.__init__(self, pool_shape=(2, 2), stride=1, padding=0)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `PoolingLayer.forward_pass(self, X, training=True)`: Forward của layer / phép tính đầu ra.
- `PoolingLayer.backward_pass(self, accum_grad)`: Lan truyền gradient về lớp trước.
- `PoolingLayer.output_shape(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `MaxPooling2D._pool_forward(self, X_col)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `MaxPooling2D._pool_backward(self, accum_grad)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `AveragePooling2D._pool_forward(self, X_col)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `AveragePooling2D._pool_backward(self, accum_grad)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `ConstantPadding2D.__init__(self, padding, padding_value=0)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `ConstantPadding2D.forward_pass(self, X, training=True)`: Forward của layer / phép tính đầu ra.
- `ConstantPadding2D.backward_pass(self, accum_grad)`: Lan truyền gradient về lớp trước.
- `ConstantPadding2D.output_shape(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `ZeroPadding2D.__init__(self, padding)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Flatten.__init__(self, input_shape=None)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Flatten.forward_pass(self, X, training=True)`: Forward của layer / phép tính đầu ra.
- `Flatten.backward_pass(self, accum_grad)`: Lan truyền gradient về lớp trước.
- `Flatten.output_shape(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `UpSampling2D.__init__(self, size=(2, 2), input_shape=None)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `UpSampling2D.forward_pass(self, X, training=True)`: Forward của layer / phép tính đầu ra.
- `UpSampling2D.backward_pass(self, accum_grad)`: Lan truyền gradient về lớp trước.
- `UpSampling2D.output_shape(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Reshape.__init__(self, shape, input_shape=None)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Reshape.forward_pass(self, X, training=True)`: Forward của layer / phép tính đầu ra.
- `Reshape.backward_pass(self, accum_grad)`: Lan truyền gradient về lớp trước.
- `Reshape.output_shape(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Dropout.__init__(self, p=0.2)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Dropout.forward_pass(self, X, training=True)`: Forward của layer / phép tính đầu ra.
- `Dropout.backward_pass(self, accum_grad)`: Lan truyền gradient về lớp trước.
- `Dropout.output_shape(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Activation.__init__(self, name)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Activation.layer_name(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Activation.forward_pass(self, X, training=True)`: Forward của layer / phép tính đầu ra.
- `Activation.backward_pass(self, accum_grad)`: Lan truyền gradient về lớp trước.
- `Activation.output_shape(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `determine_padding(filter_shape, output_shape='same')`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `get_im2col_indices(images_shape, filter_shape, padding, stride=1)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `image_to_column(images, filter_shape, stride, output_shape='same')`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `column_to_image(cols, images_shape, filter_shape, stride, output_shape='same')`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show deep_learning/layers
python practice/run.py test deep_learning/layers
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Dense(2) với input (4,3) -> (4,2); gradient shape giữ đúng.

## 7. Cạm bẫy thường gặp

Không cần hoàn thiện Conv/RNN trước khi kiểm thử Dense.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/deep_learning/layers.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
