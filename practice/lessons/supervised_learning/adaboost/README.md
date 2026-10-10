# AdaBoost

**Module ID:** `supervised_learning/adaboost`  
**Mức độ:** 04 Ensemble  
**Mục tiêu:** Huấn luyện tuần tự các weak learners với sample weights.

## 1. Kiến thức toán học cần hiểu

ε_t=Σ_i w_i[y_i≠h_t(x_i)]; α_t=0.5 ln((1−ε_t)/ε_t); w_i←w_i exp(−α_t y_i h_t(x_i)).

## 2. Đầu vào / đầu ra

fit(X,y); predict(X)->(n,) (y ∈ {-1,+1}).

## 3. Từng bước tự implement

1. **Bước 1:** Viết decision stump tìm feature/threshold/polarity.
2. **Bước 2:** Khởi tạo sample weights đồng đều.
3. **Bước 3:** Tính weighted error và learner weight alpha.
4. **Bước 4:** Cập nhật/chuẩn hóa sample weights.
5. **Bước 5:** Gộp sign của weighted votes.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/adaboost.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `DecisionStump.__init__(self)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Adaboost.__init__(self, n_clf=5)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Adaboost.fit(self, X, y)`: Ước lượng tham số từ tập huấn luyện.
- `Adaboost.predict(self, X)`: Dự đoán nhãn, giá trị hoặc cụm cho dữ liệu đầu vào.
- `main()`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/adaboost
python practice/run.py test supervised_learning/adaboost
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Toy classification với ít stump > 0.8 accuracy.

## 7. Cạm bẫy thường gặp

Chặn epsilon ở (eps, 1-eps); quy ước nhãn -1/+1.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/adaboost.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
