# Neuroevolution

**Module ID:** `supervised_learning/neuroevolution`  
**Mức độ:** 06 Advanced  
**Mục tiêu:** Tối ưu trọng số mạng bằng population-based genetic operators.

## 1. Kiến thức toán học cần hiểu

fitness=f(θ); θ_child=crossover(θ_parentA,θ_parentB)+mutation.

## 2. Đầu vào / đầu ra

evolve(X,y,n_generations) -> model hoặc params tốt nhất.

## 3. Từng bước tự implement

1. **Bước 1:** Xây param vector từ model_builder.
2. **Bước 2:** Khởi tạo population, fitness.
3. **Bước 3:** Selection top parents.
4. **Bước 4:** Crossover và random mutation.
5. **Bước 5:** Vòng lặp generations, chọn model tốt nhất.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/neuroevolution.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `Neuroevolution.__init__(self, population_size, mutation_rate, model_builder)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `Neuroevolution._build_model(self, id)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Neuroevolution._initialize_population(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Neuroevolution._mutate(self, individual, var=1)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Neuroevolution._inherit_weights(self, child, parent)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Neuroevolution._crossover(self, parent1, parent2)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Neuroevolution._calculate_fitness(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `Neuroevolution.evolve(self, X, y, n_generations)`: Lặp quá trình tối ưu tiến hóa.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/neuroevolution
python practice/run.py test supervised_learning/neuroevolution
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Fitness tốt hơn random khi generations tăng trên bài nhỏ.

## 7. Cạm bẫy thường gặp

Phụ thuộc khái niệm model_builder; student.py không import model mạng từ repo.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/neuroevolution.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
