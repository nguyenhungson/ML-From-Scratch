# LDA classification

**Module ID:** `supervised_learning/linear_discriminant_analysis`  
**Mức độ:** 03 Supervised  
**Mục tiêu:** Chiếu dữ liệu và phân lớp với Gaussian shared covariance.

## 1. Kiến thức toán học cần hiểu

w=Σ⁻¹(μ₁−μ₀); log discriminant δ_c(x)=xᵀΣ⁻¹μ_c−½μ_cᵀΣ⁻¹μ_c+log π_c.

## 2. Đầu vào / đầu ra

fit(X,y), predict(X); transform(X,y) theo API module gốc.

## 3. Từng bước tự implement

1. **Bước 1:** Tính class means và class priors.
2. **Bước 2:** Tính shared within-class covariance.
3. **Bước 3:** Sử dụng solve/pinv ổn định.
4. **Bước 4:** Viết decision score và predict.
5. **Bước 5:** Kiểm tra hai lớp trên dữ liệu Gaussian.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/linear_discriminant_analysis.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `LDA.__init__(self)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `LDA.transform(self, X, y)`: Chiếu/biến đổi biểu diễn dữ liệu.
- `LDA.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `LDA.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/linear_discriminant_analysis
python practice/run.py test supervised_learning/linear_discriminant_analysis
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Hai đám mây Gaussian có means khác nhau cho accuracy cao.

## 7. Cạm bẫy thường gặp

LDA classifier khác PCA; tránh nghịch đảo trực tiếp khi covariance suy biến.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/linear_discriminant_analysis.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
