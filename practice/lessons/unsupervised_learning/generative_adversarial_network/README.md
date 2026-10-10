# Generative Adversarial Network (GAN)

**Module ID:** `unsupervised_learning/generative_adversarial_network`  
**Mức độ:** 07 Deep Generative  
**Mục tiêu:** Huấn luyện generator/discriminator đối kháng cơ bản.

## 1. Kiến thức toán học cần hiểu

min_G max_D E[log D(x)]+E[log(1−D(G(z)))].

## 2. Đầu vào / đầu ra

train(n_epochs,batch_size,save_interval); dùng dữ liệu synthetic 2D trước ảnh.

## 3. Từng bước tự implement

1. **Bước 1:** Khởi tạo generator z→sample và discriminator sample→probability.
2. **Bước 2:** Tạo minibatch real, generated samples.
3. **Bước 3:** Update D bằng real/fake BCE.
4. **Bước 4:** Update G để fool discriminator.
5. **Bước 5:** Log losses và theo dõi mode collapse.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/unsupervised_learning/generative_adversarial_network.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `GAN.__init__(self)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `GAN.build_generator(self, optimizer, loss_function)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `GAN.build_discriminator(self, optimizer, loss_function)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `GAN.train(self, n_epochs, batch_size=128, save_interval=50)`: Triển khai vòng lặp huấn luyện.
- `GAN.save_imgs(self, epoch)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show unsupervised_learning/generative_adversarial_network
python practice/run.py test unsupervised_learning/generative_adversarial_network
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Sample shape đúng; D và G đều nhận gradient.

## 7. Cạm bẫy thường gặp

Module này ở mức đề án nâng cao: tests không thể xác nhận GAN học tốt chỉ bằng shape.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/unsupervised_learning/generative_adversarial_network.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
