# Gợi ý theo 3 cấp — Neural Network Layers

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Bắt đầu Layer interface (initialize, forward_pass, backward_pass). Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

Dense: Y=XW+b; dW=Xᵀ dY; dX=dY Wᵀ. Conv: correlation patches với kernels.

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Dense(2) với input (4,3) -> (4,2); gradient shape giữ đúng.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
