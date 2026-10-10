# Gợi ý theo 3 cấp — Perceptron classifier

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Kiểm tra y thuộc {-1,+1} hoặc mã hóa từ {0,1}. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

ŷ=sign(wᵀx+b); cập nhật khi nhãn sai: w←w+η yx, b←b+ηy (y ∈ {−1,+1}).

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: AND logic hoặc 2 cụm phân tách tuyến tính.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
