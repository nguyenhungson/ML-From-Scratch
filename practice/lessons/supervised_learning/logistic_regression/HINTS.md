# Gợi ý theo 3 cấp — Logistic Regression

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Triển khai sigmoid ổn định số học. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

p=σ(Xw+b), σ(z)=1/(1+e^(−z)); ∇w=Xᵀ(p−y)/n; BCE=−mean[y log p+(1−y) log(1−p)].

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Tách hai cụm dễ để accuracy > 0.9.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
