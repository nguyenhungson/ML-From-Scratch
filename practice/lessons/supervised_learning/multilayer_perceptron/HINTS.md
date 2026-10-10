# Gợi ý theo 3 cấp — MLP từ đầu

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Khởi tạo W1,b1,W2,b2 đúng shape. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

h=σ(XW₁+b₁); ŷ=softmax(hW₂+b₂); δ₂=ŷ−Y; δ₁=(δ₂W₂ᵀ)⊙σ′(z₁).

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: XOR 4 điểm với nhiều epochs/seed có thể học đạt accuracy cao.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
