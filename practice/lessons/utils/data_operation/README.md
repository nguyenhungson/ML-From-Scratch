# Các phép toán nền tảng cho ML

**Module ID:** `utils/data_operation`  
**Mức độ:** 01 Cơ sở  
**Mục tiêu:** Cài đặt các metric/thống kê dùng trong các thuật toán.

## 1. Kiến thức toán học cần hiểu

MSE=mean((y−ŷ)²); entropy H(Y)=−Σp log₂p; covariance Cov(X,Y)=Σ(x−x̄)(y−ȳ)/(n−1).

## 2. Đầu vào / đầu ra

X: (n,d); y: (n,); kết quả scalar hoặc matrix.

## 3. Từng bước tự implement

1. **Bước 1:** Viết euclidean_distance, mse, accuracy.
2. **Bước 2:** Đếm tần suất nhãn trước khi tính entropy.
3. **Bước 3:** Tính variance, standard deviation, covariance theo trục features.
4. **Bước 4:** Tính correlation từ covariance và std; xử lý std bằng 0.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/utils/data_operation.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `calculate_entropy(y)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `mean_squared_error(y_true, y_pred)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `calculate_variance(X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `calculate_std_dev(X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `euclidean_distance(x1, x2)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `accuracy_score(y_true, y_pred)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `calculate_covariance_matrix(X, Y=None)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `calculate_correlation_matrix(X, Y=None)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show utils/data_operation
python practice/run.py test utils/data_operation
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Test khoảng cách 3-4-5, MSE=0 cho dự đoán đúng, entropy nhãn cân bằng.

## 7. Cạm bẫy thường gặp

Chú ý ddof=0 hay 1; nhất quán trong mọi bài kiểm thử.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/utils/data_operation.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
