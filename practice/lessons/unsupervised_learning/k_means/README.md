# K-means clustering

**Module ID:** `unsupervised_learning/k_means`  
**Mức độ:** 02 Unsupervised  
**Mục tiêu:** Gom cụm dựa trên centroids và khoảng cách Euclid.

## 1. Kiến thức toán học cần hiểu

c_i=argmin_j ||x_i−μ_j||²; μ_j=mean({x_i:c_i=j}).

## 2. Đầu vào / đầu ra

predict(X:(n,d))->label (n,) theo API repo gốc (fit+predict gộp).

## 3. Từng bước tự implement

1. **Bước 1:** Chọn k centers từ dữ liệu.
2. **Bước 2:** Gán nhãn vào center gần nhất.
3. **Bước 3:** Cập nhật center bằng mean.
4. **Bước 4:** Xử lý empty clusters.
5. **Bước 5:** Dừng khi centers không đổi hoặc max_iterations.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/unsupervised_learning/k_means.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `KMeans.__init__(self, k=2, max_iterations=500)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `KMeans._init_random_centroids(self, X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `KMeans._closest_centroid(self, sample, centroids)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `KMeans._create_clusters(self, centroids, X)`: Gán mẫu vào từng cụm.
- `KMeans._calculate_centroids(self, clusters, X)`: Tính trung tâm cụm.
- `KMeans._get_cluster_labels(self, clusters, X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `KMeans.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show unsupervised_learning/k_means
python practice/run.py test unsupervised_learning/k_means
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Bốn điểm quanh (0,0), bốn điểm quanh (10,10) chia thành 2 cụm.

## 7. Cạm bẫy thường gặp

Cluster IDs có thể hoán vị; không so nhãn theo 0/1 cố định.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/unsupervised_learning/k_means.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
