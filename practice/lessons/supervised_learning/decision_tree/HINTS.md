# Gợi ý theo 3 cấp — Decision Tree classification/regression

Chỉ mở khi bạn đã thử tự làm.

## Gợi ý 1 — Chia nhỏ bài

Thiết kế DecisionNode lưu feature, threshold, children hoặc leaf value. Hãy viết ví dụ bằng tay trên 3–6 dòng dữ liệu trước.

## Gợi ý 2 — Chuyển công thức thành phép tính mảng

Classification: Gini=1−Σp_c²; IG=H(parent)−Σ(n_child/n)H(child); Regression: giảm phương sai.

Chú ý shape của từng biểu thức trước khi viết NumPy. Kiểm tra bằng một ví dụ nhỏ có kết quả tính tay.

## Gợi ý 3 — Debug từng bước

- In shapes, min/max, dtype và các giá trị không hữu hạn (NaN/inf).
- Kiểm tra invariant: Cây độ sâu vừa phải giải được bài OR/AND, tree regression trả mean ở leaf.
- Cố định random seed để tái hiện lỗi; chạy test của riêng lesson.
- Đọc source gốc **sau** khi đã thử ít nhất một cách giải.
