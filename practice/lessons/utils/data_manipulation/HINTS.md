# Gợi ý theo 3 cấp — Tiền xử lý và chia dữ liệu

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Phân biệt fit preprocessing trên train và transform test để tránh leakage. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

z=(x−μ)/σ; x_normalized=x/||x||; train/test dùng cùng một phép hoán vị chỉ số.

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Chia dữ liệu 6 mẫu; kiểm tra union là toàn bộ mẫu, intersection rỗng.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
