# Gợi ý theo 3 cấp — Gaussian Mixture Model (EM)

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Khởi tạo mixture weights/means/covariances. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

γ_ik=π_k N(x_i|μ_k,Σ_k)/Σ_jπ_j N(x_i|μ_j,Σ_j); μ_k=Σ_iγ_ikx_i/Σ_iγ_ik.

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Hai cụm Gaussian tách xa được gán khác component.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
