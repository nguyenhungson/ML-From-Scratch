# Tiền xử lý và chia dữ liệu

**Module ID:** `utils/data_manipulation`  
**Mức độ:** 01 Cơ sở  
**Mục tiêu:** Viết từ đầu các phép shuffle, train/test split, normalization, one-hot, polynomial features và mini-batch.

## 1. Kiến thức toán học cần hiểu

z=(x−μ)/σ; x_normalized=x/||x||; train/test dùng cùng một phép hoán vị chỉ số.

## 2. Đầu vào / đầu ra

X: (n,d), y: (n,); thao tác đều theo chiều samples.

## 3. Từng bước tự implement

1. **Bước 1:** Phân biệt fit preprocessing trên train và transform test để tránh leakage.
2. **Bước 2:** Dùng RNG seed giúp reproducible.
3. **Bước 3:** Viết shuffle, split, batch_iterator trên chỉ số.
4. **Bước 4:** Triển khai chuẩn hóa, encode, polynomial features, k-fold.
5. **Bước 5:** Kiểm thử độ dài, shape, tỷ lệ split, không trùng train/test.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/utils/data_manipulation.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `shuffle_data(X, y, seed=None)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `batch_iterator(X, y=None, batch_size=64)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `divide_on_feature(X, feature_i, threshold)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `polynomial_features(X, degree)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `get_random_subsets(X, y, n_subsets, replacements=True)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `normalize(X, axis=-1, order=2)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `standardize(X)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `train_test_split(X, y, test_size=0.5, shuffle=True, seed=None)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `k_fold_cross_validation_sets(X, y, k, shuffle=True)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `to_categorical(x, n_col=None)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `to_nominal(x)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `make_diagonal(x)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show utils/data_manipulation
python practice/run.py test utils/data_manipulation
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Chia dữ liệu 6 mẫu; kiểm tra union là toàn bộ mẫu, intersection rỗng.

## 7. Cạm bẫy thường gặp

Không tính mean/std từ tập test khi triển khai production pipeline.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/utils/data_manipulation.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
