# Gợi ý theo 3 cấp — AdaBoost

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Viết decision stump tìm feature/threshold/polarity. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

ε_t=Σ_i w_i[y_i≠h_t(x_i)]; α_t=0.5 ln((1−ε_t)/ε_t); w_i←w_i exp(−α_t y_i h_t(x_i)).

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Toy classification với ít stump > 0.8 accuracy.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
