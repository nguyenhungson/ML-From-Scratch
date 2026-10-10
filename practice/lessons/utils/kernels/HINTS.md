# Gợi ý theo 3 cấp — Kernel functions

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Chuẩn hóa vector/matrix đầu vào bằng np.asarray. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

linear: K(x,z)=xᵀz; polynomial: K(x,z)=(xᵀz+c)^p; RBF: K(x,z)=exp(-γ||x-z||²).

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: So sánh với tích vô hướng và công thức tính tay.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
