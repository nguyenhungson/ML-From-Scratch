# Multiclass LDA projection

**Module ID:** `supervised_learning/multi_class_lda`  
**Mức độ:** 04 Supervised  
**Mục tiêu:** Học phép chiếu Fisher giữ thông tin phân biệt các lớp.

## 1. Kiến thức toán học cần hiểu

S_w=Σ_cΣ_{x∈c}(x−μ_c)(x−μ_c)ᵀ; S_b=Σ_c n_c(μ_c−μ)(μ_c−μ)ᵀ; eigen(S_w⁻¹ S_b).

## 2. Đầu vào / đầu ra

transform(X,y,n_components)->(n,n_components).

## 3. Từng bước tự implement

1. **Bước 1:** Tính class means và overall mean.
2. **Bước 2:** Tính S_w và S_b.
3. **Bước 3:** Giải generalized eigenvectors.
4. **Bước 4:** Chọn tối đa min(d,n_classes−1) components.
5. **Bước 5:** Transform dựa trên eigenvectors.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/multi_class_lda.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `MultiClassLDA.__init__(self, solver='svd')`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `MultiClassLDA._calculate_scatter_matrices(self, X, y)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `MultiClassLDA.transform(self, X, y, n_components)`: Chiếu/biến đổi biểu diễn dữ liệu.
- `MultiClassLDA.plot_in_2d(self, X, y, title=None)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/multi_class_lda
python practice/run.py test supervised_learning/multi_class_lda
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Trên dữ liệu 3 lớp, output đúng shape và giữ phương sai giữa lớp.

## 7. Cạm bẫy thường gặp

S_w có thể singular: regularize/pinv.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/multi_class_lda.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
