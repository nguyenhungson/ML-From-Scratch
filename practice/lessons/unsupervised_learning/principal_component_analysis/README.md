# Principal Component Analysis (PCA)

**Module ID:** `unsupervised_learning/principal_component_analysis`  
**Mức độ:** 02 Unsupervised  
**Mục tiêu:** Chiếu dữ liệu lên các trục phương sai lớn nhất.

## 1. Kiến thức toán học cần hiểu

X_c=X−μ; Cov=X_cᵀX_c/(n−1); W=eigenvectors của Cov theo eigenvalue giảm dần; Z=X_cW_k.

## 2. Đầu vào / đầu ra

transform(X,n_components)->(n,n_components).

## 3. Từng bước tự implement

1. **Bước 1:** Mean center theo feature.
2. **Bước 2:** Tính covariance hoặc SVD.
3. **Bước 3:** Sắp xếp eigenvectors theo eigenvalues giảm dần.
4. **Bước 4:** Chọn n_components.
5. **Bước 5:** Transform và tùy chọn reconstruction.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/unsupervised_learning/principal_component_analysis.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `PCA.transform(self, X, n_components)`: Chiếu/biến đổi biểu diễn dữ liệu.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show unsupervised_learning/principal_component_analysis
python practice/run.py test unsupervised_learning/principal_component_analysis
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Điểm gần đường y=2x cho thành phần đầu có variance lớn.

## 7. Cạm bẫy thường gặp

Phải center trước; eigenvector ± cùng biểu diễn một trục.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/unsupervised_learning/principal_component_analysis.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
