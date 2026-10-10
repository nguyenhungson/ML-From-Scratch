# Gợi ý theo 3 cấp — Hồi quy tuyến tính và regularization

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Viết Regression base cùng intercept. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

MSE=mean((Xw−y)²); Ridge: MSE+λ||w||²₂; Lasso: MSE+λ||w||₁; Elastic Net: L1+L2.

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Với y=2x+1, dự đoán sát kết quả; weight shrinkage tăng khi lambda tăng.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
