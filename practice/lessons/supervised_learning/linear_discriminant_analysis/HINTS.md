# Gợi ý theo 3 cấp — LDA classification

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Tính class means và class priors. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

w=Σ⁻¹(μ₁−μ₀); log discriminant δ_c(x)=xᵀΣ⁻¹μ_c−½μ_cᵀΣ⁻¹μ_c+log π_c.

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Hai đám mây Gaussian có means khác nhau cho accuracy cao.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
