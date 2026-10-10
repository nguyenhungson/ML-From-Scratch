# Restricted Boltzmann Machine

**Module ID:** `unsupervised_learning/restricted_boltzmann_machine`  
**Mức độ:** 06 Deep Generative  
**Mục tiêu:** Huấn luyện model Boltzmann hai lớp với Contrastive Divergence.

## 1. Kiến thức toán học cần hiểu

E(v,h)=−bᵀv−cᵀh−vᵀWh; CD-1: ΔW∝v₀h₀ᵀ−v₁h₁ᵀ.

## 2. Đầu vào / đầu ra

fit(X,y=None) và reconstruct(X)->X_hat.

## 3. Từng bước tự implement

1. **Bước 1:** Khởi tạo W, visible bias, hidden bias.
2. **Bước 2:** Sample hidden và reconstruct visible bằng sigmoid.
3. **Bước 3:** CD-k positive/negative phases.
4. **Bước 4:** Update parameters theo minibatches.
5. **Bước 5:** Theo dõi reconstruction error.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/unsupervised_learning/restricted_boltzmann_machine.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `RBM.__init__(self, n_hidden=128, learning_rate=0.1, batch_size=10, n_iterations=100)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `RBM._initialize_weights(self, X)`: Tạo trọng số ban đầu với shape đúng.
- `RBM.fit(self, X, y=None)`: Ước lượng tham số từ tập huấn luyện.
- `RBM._sample(self, X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `RBM.reconstruct(self, X)`: Khôi phục đầu vào từ latent/hidden representation.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show unsupervised_learning/restricted_boltzmann_machine
python practice/run.py test unsupervised_learning/restricted_boltzmann_machine
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Dữ liệu Bernoulli toy, reconstruction shape bằng X và lỗi giảm.

## 7. Cạm bẫy thường gặp

Phân biệt xác suất kích hoạt và mẫu Bernoulli binary.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/unsupervised_learning/restricted_boltzmann_machine.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
