# Genetic Algorithm

**Module ID:** `unsupervised_learning/genetic_algorithm`  
**Mức độ:** 04 Optimization  
**Mục tiêu:** Tìm target string bằng tiến hóa quần thể.

## 1. Kiến thức toán học cần hiểu

fitness= số vị trí ký tự khớp target; selection+crossover+mutation.

## 2. Đầu vào / đầu ra

run(iterations) -> best string hoặc fitness.

## 3. Từng bước tự implement

1. **Bước 1:** Tạo population random strings.
2. **Bước 2:** Đánh giá fitness mỗi cá thể.
3. **Bước 3:** Chọn parents, crossover.
4. **Bước 4:** Mutation theo tỷ lệ.
5. **Bước 5:** Giữ best individual tới convergence.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/unsupervised_learning/genetic_algorithm.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `GeneticAlgorithm.__init__(self, target_string, population_size, mutation_rate)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `GeneticAlgorithm._initialize(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `GeneticAlgorithm._calculate_fitness(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `GeneticAlgorithm._mutate(self, individual)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `GeneticAlgorithm._crossover(self, parent1, parent2)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `GeneticAlgorithm.run(self, iterations)`: Chạy thuật toán đến điều kiện dừng.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show unsupervised_learning/genetic_algorithm
python practice/run.py test unsupervised_learning/genetic_algorithm
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Với target "ABC" tìm lời giải khi iterations đủ lớn và seed cố định.

## 7. Cạm bẫy thường gặp

Tránh thay đổi mutable parents tại chỗ.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/unsupervised_learning/genetic_algorithm.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
