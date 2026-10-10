# Gợi ý theo 3 cấp — Activation Functions

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Cài đặt sigmoid, tanh, relu, leaky relu. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

σ(x)=1/(1+e^-x), σ′=σ(1−σ); ReLU=max(0,x); tanh′=1−tanh²(x); softmax(x)_i=e^(x_i−max x)/Σ_j e^(x_j−max x).

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: σ(0)=0.5, ReLU(-1)=0, softmax mỗi row tổng=1.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
