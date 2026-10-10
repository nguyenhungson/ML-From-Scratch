# Gợi ý theo 3 cấp — Gradient Boosting

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Khởi tạo prediction theo mean target hoặc logits. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

F_m(x)=F_{m−1}(x)+η h_m(x); square loss pseudo-residual r_i=y_i−F_{m−1}(x_i).

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Hồi quy y=x² trên dữ liệu nhỏ; MSE giảm theo số estimators.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
