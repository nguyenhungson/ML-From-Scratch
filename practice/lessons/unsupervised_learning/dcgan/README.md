# Deep Convolutional GAN

**Module ID:** `unsupervised_learning/dcgan`  
**Mức độ:** 07 Deep Generative  
**Mục tiêu:** Mở rộng GAN bằng convolution/transposed convolution.

## 1. Kiến thức toán học cần hiểu

D(x)=CNN classifier; G(z)=transposed-conv decoder; adversarial BCE objective.

## 2. Đầu vào / đầu ra

train(epochs,batch_size,save_interval); ảnh normalized vào [-1,1].

## 3. Từng bước tự implement

1. **Bước 1:** Implement conv layers và upsampling.
2. **Bước 2:** Xây generator/discriminator theo shape ảnh.
3. **Bước 3:** Kiểm tra output shape và range của pixel.
4. **Bước 4:** Train D rồi train G.
5. **Bước 5:** Visualize sample grid và lưu checkpoints.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/unsupervised_learning/dcgan.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `DCGAN.__init__(self)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `DCGAN.build_generator(self, optimizer, loss_function)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `DCGAN.build_discriminator(self, optimizer, loss_function)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `DCGAN.train(self, epochs, batch_size=128, save_interval=50)`: Triển khai vòng lặp huấn luyện.
- `DCGAN.save_imgs(self, epoch)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show unsupervised_learning/dcgan
python practice/run.py test unsupervised_learning/dcgan
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Tạo batch ảnh mock và verify dimensions.

## 7. Cạm bẫy thường gặp

Đọc deep_learning/layers trước; gradient transpose convolution phức tạp.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/unsupervised_learning/dcgan.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
