# Trực quan hóa kết quả

**Module ID:** `utils/misc`  
**Mức độ:** 02 Công cụ  
**Mục tiêu:** Tự tạo các hàm vẽ dự đoán/điểm dữ liệu; đây là module tiện ích chứ không phải thuật toán học.

## 1. Kiến thức toán học cần hiểu

Regression plot: scatter(x,y) cùng đường dự đoán ŷ(x).

## 2. Đầu vào / đầu ra

X 1D/2D/3D, y hoặc class labels; đầu ra matplotlib figure hoặc file ảnh.

## 3. Từng bước tự implement

1. **Bước 1:** Tách chuẩn bị dữ liệu khỏi vẽ.
2. **Bước 2:** Kiểm tra X có đủ chiều cần thiết.
3. **Bước 3:** Hỗ trợ không hiển thị GUI trong CI và lưu ảnh.
4. **Bước 4:** Thêm nhãn trục/legend và kết quả định lượng.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/utils/misc.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `Plot.__init__(self)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Plot._transform(self, X, dim)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Plot.plot_regression(self, lines, title, axis_labels=None, mse=None, scatter=None, legend={'type': 'lines', 'loc': 'lower right'})`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Plot.plot_in_2d(self, X, y=None, title=None, accuracy=None, legend_labels=None)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Plot.plot_in_3d(self, X, y=None)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show utils/misc
python practice/run.py test utils/misc
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Smoke test tạo figure với backend Agg.

## 7. Cạm bẫy thường gặp

Module này có thể dùng matplotlib; các bài ML khác chỉ cần numpy.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/utils/misc.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
