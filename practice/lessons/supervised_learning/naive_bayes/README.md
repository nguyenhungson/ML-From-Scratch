# Gaussian Naive Bayes

**Module ID:** `supervised_learning/naive_bayes`  
**Mức độ:** 02 Supervised  
**Mục tiêu:** Ước lượng posterior theo giả định độc lập có điều kiện.

## 1. Kiến thức toán học cần hiểu

log P(c|x) ∝ log P(c)+Σ_j[-0.5log(2πσ²_cj)−(x_j−μ_cj)²/(2σ²_cj)].

## 2. Đầu vào / đầu ra

fit(X,y) và predict(X)->(n,).

## 3. Từng bước tự implement

1. **Bước 1:** Liệt kê class labels.
2. **Bước 2:** Ước lượng class prior P(c), mean, variance theo từng feature.
3. **Bước 3:** Thêm epsilon vào variance.
4. **Bước 4:** Tính log likelihood rồi argmax.
5. **Bước 5:** Dự đoán với nhiều classes.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/naive_bayes.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `NaiveBayes.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `NaiveBayes._calculate_likelihood(self, mean, var, x)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `NaiveBayes._calculate_prior(self, c)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `NaiveBayes._classify(self, sample)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `NaiveBayes.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/naive_bayes
python practice/run.py test supervised_learning/naive_bayes
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Hai cụm Gaussian cách xa nhau cho dự đoán chính xác.

## 7. Cạm bẫy thường gặp

Tính xác suất ở log-space để tránh underflow.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/naive_bayes.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
