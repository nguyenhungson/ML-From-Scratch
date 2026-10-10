# K-medoids / PAM

**Module ID:** `unsupervised_learning/partitioning_around_medoids`  
**Mức độ:** 03 Unsupervised  
**Mục tiêu:** Gom cụm với centers bắt buộc là các quan sát trong tập dữ liệu.

## 1. Kiến thức toán học cần hiểu

Objective=Σ_i min_{m∈M} d(x_i,m), M ⊂ observations.

## 2. Đầu vào / đầu ra

predict(X)->(n,) label.

## 3. Từng bước tự implement

1. **Bước 1:** Lấy k medoids ngẫu nhiên.
2. **Bước 2:** Gán mẫu vào medoid gần nhất.
3. **Bước 3:** Thử swap medoid với điểm ngoài để giảm cost.
4. **Bước 4:** Dừng khi không có swap cải thiện.
5. **Bước 5:** Trả cluster assignment.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/unsupervised_learning/partitioning_around_medoids.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `PAM.__init__(self, k=2)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `PAM._init_random_medoids(self, X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `PAM._closest_medoid(self, sample, medoids)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `PAM._create_clusters(self, X, medoids)`: Gán mẫu vào từng cụm.
- `PAM._calculate_cost(self, X, clusters, medoids)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `PAM._get_non_medoids(self, X, medoids)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `PAM._get_cluster_labels(self, clusters, X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `PAM.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show unsupervised_learning/partitioning_around_medoids
python practice/run.py test unsupervised_learning/partitioning_around_medoids
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Medoid luôn bằng một hàng của X; outlier ít ảnh hưởng hơn k-means.

## 7. Cạm bẫy thường gặp

Không dùng trung bình cụm làm medoid.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/unsupervised_learning/partitioning_around_medoids.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
