# DBSCAN clustering

**Module ID:** `unsupervised_learning/dbscan`  
**Mức độ:** 03 Unsupervised  
**Mục tiêu:** Tìm density-connected clusters và nhận diện noise.

## 1. Kiến thức toán học cần hiểu

N_ε(x)={z:||x−z||≤ε}; core point nếu |N_ε(x)|≥min_samples.

## 2. Đầu vào / đầu ra

predict(X)->(n,) labels.

## 3. Từng bước tự implement

1. **Bước 1:** Với mỗi điểm, tìm epsilon-neighbors.
2. **Bước 2:** Phân loại core/border/noise.
3. **Bước 3:** Duyệt BFS/DFS expand cluster từ core.
4. **Bước 4:** Đánh nhãn noise=-1.
5. **Bước 5:** Trả labels có thể gồm -1 và >=0.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/unsupervised_learning/dbscan.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `DBSCAN.__init__(self, eps=1, min_samples=5)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `DBSCAN._get_neighbors(self, sample_i)`: Lấy neighbors theo metric và bán kính.
- `DBSCAN._expand_cluster(self, sample_i, neighbors)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `DBSCAN._get_cluster_labels(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `DBSCAN.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show unsupervised_learning/dbscan
python practice/run.py test unsupervised_learning/dbscan
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Hai cụm gần nhau theo eps, một outlier phải nhãn -1.

## 7. Cạm bẫy thường gặp

min_samples thường tính cả điểm đang xét; noise có thể được bổ sung vào cluster.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/unsupervised_learning/dbscan.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
