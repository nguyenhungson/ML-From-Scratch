# Gợi ý theo 3 cấp — Optimizers: SGD, Adam, RMSprop

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Viết SGD và momentum. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

SGD: w←w−ηg; momentum v←μv+g; Adam m←β₁m+(1−β₁)g, v←β₂v+(1−β₂)g².

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Với w=[1,-1] và g=2w, một bước SGD nhỏ giảm ||w||.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
