# Gợi ý theo 3 cấp — Multiclass LDA projection

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Tính class means và overall mean. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

S_w=Σ_cΣ_{x∈c}(x−μ_c)(x−μ_c)ᵀ; S_b=Σ_c n_c(μ_c−μ)(μ_c−μ)ᵀ; eigen(S_w⁻¹ S_b).

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Trên dữ liệu 3 lớp, output đúng shape và giữ phương sai giữa lớp.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
