# Gợi ý theo 3 cấp — Các phép toán nền tảng cho ML

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Viết euclidean_distance, mse, accuracy. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

MSE=mean((y−ŷ)²); entropy H(Y)=−Σp log₂p; covariance Cov(X,Y)=Σ(x−x̄)(y−ȳ)/(n−1).

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Test khoảng cách 3-4-5, MSE=0 cho dự đoán đúng, entropy nhãn cân bằng.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
