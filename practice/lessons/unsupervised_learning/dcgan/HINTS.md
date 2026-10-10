# Gợi ý theo 3 cấp — Deep Convolutional GAN

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Implement conv layers và upsampling. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

D(x)=CNN classifier; G(z)=transposed-conv decoder; adversarial BCE objective.

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Tạo batch ảnh mock và verify dimensions.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
