# Autoencoder

**Module ID:** `unsupervised_learning/autoencoder`  
**Mức độ:** 06 Deep Generative  
**Mục tiêu:** Học compressed latent representation rồi tái tạo dữ liệu.

## 1. Kiến thức toán học cần hiểu

z=f_encoder(X); X̂=g_decoder(z); minimize ||X−X̂||².

## 2. Đầu vào / đầu ra

train(n_epochs,batch_size) API gốc; tự bổ sung fit(X) nếu muốn học độc lập không dùng dataset nội bộ.

## 3. Từng bước tự implement

1. **Bước 1:** Tự viết dense+activation hoặc chọn đơn giản tuyến tính đầu tiên.
2. **Bước 2:** Encoder n→latent, Decoder latent→n.
3. **Bước 3:** Tính reconstruction loss/backprop.
4. **Bước 4:** Train loop batches.
5. **Bước 5:** Theo dõi reconstructions.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/unsupervised_learning/autoencoder.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `Autoencoder.__init__(self)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Autoencoder.build_encoder(self, optimizer, loss_function)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Autoencoder.build_decoder(self, optimizer, loss_function)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Autoencoder.train(self, n_epochs, batch_size=128, save_interval=50)`: Triển khai vòng lặp huấn luyện.
- `Autoencoder.save_imgs(self, epoch, X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show unsupervised_learning/autoencoder
python practice/run.py test unsupervised_learning/autoencoder
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Reconstruction shape bằng input và MSE giảm.

## 7. Cạm bẫy thường gặp

Không dùng X làm label class; target tái tạo chính X.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/unsupervised_learning/autoencoder.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
