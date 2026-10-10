# Gợi ý theo 3 cấp — Neural Network training engine

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Định nghĩa add() thêm layer, initialize shape. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

forward: x→L₁→⋯→L_k→ŷ; backprop: ∂L/∂h_i=(∂L/∂h_{i+1})(∂h_{i+1}/∂h_i).

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Học XOR hoặc regression nhỏ khi Dense/loss đã hoạt động.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
