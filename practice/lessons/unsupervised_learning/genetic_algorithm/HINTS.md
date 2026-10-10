# Gợi ý theo 3 cấp — Genetic Algorithm

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Tạo population random strings. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

fitness= số vị trí ký tự khớp target; selection+crossover+mutation.

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Với target "ABC" tìm lời giải khi iterations đủ lớn và seed cố định.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
