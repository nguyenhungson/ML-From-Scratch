# Kernel functions

**Module ID:** `utils/kernels`  
**Mức độ:** 01 Cơ sở  
**Mục tiêu:** Tự viết các hàm đo độ tương đồng để sử dụng trong SVM và kernel methods.

## 1. Kiến thức toán học cần hiểu

linear: K(x,z)=xᵀz; polynomial: K(x,z)=(xᵀz+c)^p; RBF: K(x,z)=exp(-γ||x-z||²).

## 2. Đầu vào / đầu ra

Theo API source gốc, mỗi hàm `linear_kernel()`, `polynomial_kernel(...)`, `rbf_kernel(...)` trả **callable** `f(x1,x2)`. Với hai vector `(d,)`, kết quả là một số vô hướng. Muốn ma trận kernel `(n,m)`, lặp theo các cặp vector hoặc vector hóa riêng; `np.inner` cũng nhận 2 ma trận.

## 3. Từng bước tự implement

1. **Bước 1:** Chuẩn hóa vector/matrix đầu vào bằng np.asarray.
2. **Bước 2:** Viết linear kernel và polynomial kernel không vòng lặp không cần thiết.
3. **Bước 3:** Viết RBF kernel từ bình phương khoảng cách Euclid của **hai vector**.
4. **Bước 4:** Thử tính đối xứng, shape và giá trị đường chéo của ma trận kernel.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/utils/kernels.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `linear_kernel(**kwargs)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `polynomial_kernel(power, coef, **kwargs)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `rbf_kernel(gamma, **kwargs)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show utils/kernels
python practice/run.py test utils/kernels
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

So sánh với tích vô hướng và công thức tính tay.

## 7. Cạm bẫy thường gặp

Cẩn thận broadcasting và gamma không âm.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/utils/kernels.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
