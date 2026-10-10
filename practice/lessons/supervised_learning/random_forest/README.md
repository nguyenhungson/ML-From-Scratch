# Random Forest

**Module ID:** `supervised_learning/random_forest`  
**Mức độ:** 04 Ensemble  
**Mục tiêu:** Huấn luyện nhiều cây trên bootstrap samples và ngẫu nhiên feature.

## 1. Kiến thức toán học cần hiểu

ŷ_class=mode(T₁(x),…,T_B(x)); bootstrap sample có hoàn lại.

## 2. Đầu vào / đầu ra

fit(X,y), predict(X)->(n,).

## 3. Từng bước tự implement

1. **Bước 1:** Tạo n_estimators bootstrap datasets.
2. **Bước 2:** Tại mỗi split lấy ngẫu nhiên subset features (hoặc train tree có feature subset).
3. **Bước 3:** Huấn luyện các cây classification.
4. **Bước 4:** Gộp kết quả majority vote.
5. **Bước 5:** So với single tree và thử seed.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/random_forest.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `RandomForest.__init__(self, n_estimators=100, max_features=None, min_samples_split=2, min_gain=0, max_depth=float('inf'))`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `RandomForest.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `RandomForest.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/random_forest
python practice/run.py test supervised_learning/random_forest
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Kết quả hình dạng đúng, có ≥2 cây, accuracy tốt trên toy dataset.

## 7. Cạm bẫy thường gặp

Tránh reuse cùng một bộ bootstrap và tránh data leakage.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/random_forest.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
