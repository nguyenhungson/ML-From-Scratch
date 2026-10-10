# Gợi ý theo 3 cấp — Support Vector Machine (kernel)

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Bắt đầu linear soft-margin hinge-loss để nắm ý tưởng. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

min_{w,b} ½||w||² + CΣ_i max(0,1−y_i(wᵀx_i+b)); kernel: f(x)=Σα_i y_iK(x_i,x)+b.

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Học 2 cụm tuyến tính tách biệt; kernel phải đối xứng.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
