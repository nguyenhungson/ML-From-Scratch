# Support Vector Machine (kernel)

**Module ID:** `supervised_learning/support_vector_machine`  
**Mức độ:** 04 Supervised  
**Mục tiêu:** Hiểu max-margin classifier và kernel decision boundary.

## 1. Kiến thức toán học cần hiểu

min_{w,b} ½||w||² + CΣ_i max(0,1−y_i(wᵀx_i+b)); kernel: f(x)=Σα_i y_iK(x_i,x)+b.

## 2. Đầu vào / đầu ra

fit(X,y), predict(X)->(n,), nhãn ±1.

## 3. Từng bước tự implement

1. **Bước 1:** Bắt đầu linear soft-margin hinge-loss để nắm ý tưởng.
2. **Bước 2:** Viết kernel matrix qua RBF/poly hoặc chọn linear.
3. **Bước 3:** Giải constrained dual hoặc dùng optimization thay thế.
4. **Bước 4:** Lưu support vectors và coefficients.
5. **Bước 5:** Dự đoán sign(decision score).

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/support_vector_machine.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `SupportVectorMachine.__init__(self, C=1, kernel=None, power=4, gamma=None, coef=4)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `SupportVectorMachine.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `SupportVectorMachine.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/support_vector_machine
python practice/run.py test supervised_learning/support_vector_machine
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Học 2 cụm tuyến tính tách biệt; kernel phải đối xứng.

## 7. Cạm bẫy thường gặp

Code gốc dùng CVXOPT. Bài độc lập có thể chọn primal SGD trước, sau đó dual solver.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/support_vector_machine.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
