# K-nearest neighbors (KNN)

**Module ID:** `supervised_learning/k_nearest_neighbors`  
**Mức độ:** 02 Supervised  
**Mục tiêu:** Dự đoán bằng khoảng cách và majority vote, không có bước tối ưu tham số.

## 1. Kiến thức toán học cần hiểu

d(x,z)=√Σ(x_j−z_j)²; ŷ=mode({y_i : i ∈ k-nearest(x)}).

## 2. Đầu vào / đầu ra

predict(X_test, X_train, y_train) -> (n_test,).

## 3. Từng bước tự implement

1. **Bước 1:** Tính distances tới mọi điểm train.
2. **Bước 2:** Lấy top-k với argsort hoặc argpartition.
3. **Bước 3:** Vote đa số, quy tắc tie-break cố định.
4. **Bước 4:** Hỗ trợ nhiều X_test và dữ liệu đa chiều.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/k_nearest_neighbors.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `KNN.__init__(self, k=5)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `KNN._vote(self, neighbor_labels)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `KNN.predict(self, X_test, X_train, y_train)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/k_nearest_neighbors
python practice/run.py test supervised_learning/k_nearest_neighbors
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

k=1 trả về nhãn láng giềng gần nhất; k=3 kiểm tra majority vote.

## 7. Cạm bẫy thường gặp

Không vote dựa trên các giá trị feature; xử lý k > n_train.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/k_nearest_neighbors.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
