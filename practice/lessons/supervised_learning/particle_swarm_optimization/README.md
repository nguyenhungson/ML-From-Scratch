# Particle Swarm Optimization (PSO)

**Module ID:** `supervised_learning/particle_swarm_optimization`  
**Mức độ:** 06 Advanced  
**Mục tiêu:** Tối ưu trọng số ML model bằng swarm search.

## 1. Kiến thức toán học cần hiểu

v←ωv+c₁r₁(pbest−x)+c₂r₂(gbest−x); x←x+v.

## 2. Đầu vào / đầu ra

evolve(X,y,n_generations) -> nghiệm tốt nhất.

## 3. Từng bước tự implement

1. **Bước 1:** Mỗi particle có position và velocity.
2. **Bước 2:** Tính fitness, cập nhật pbest/gbest.
3. **Bước 3:** Update velocity và vị trí từng particle.
4. **Bước 4:** Clamp velocity, kiểm tra convergence.
5. **Bước 5:** Dùng model_builder do người học tự truyền.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/supervised_learning/particle_swarm_optimization.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `ParticleSwarmOptimizedNN.__init__(self, population_size, model_builder, inertia_weight=0.8, cognitive_weight=2, social_weight=2, max_velocity=20)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `ParticleSwarmOptimizedNN._build_model(self, id)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `ParticleSwarmOptimizedNN._initialize_population(self)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `ParticleSwarmOptimizedNN._update_weights(self, individual)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `ParticleSwarmOptimizedNN._calculate_fitness(self, individual)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `ParticleSwarmOptimizedNN.evolve(self, X, y, n_generations)`: Lặp quá trình tối ưu tiến hóa.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show supervised_learning/particle_swarm_optimization
python practice/run.py test supervised_learning/particle_swarm_optimization
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Hàm mục tiêu đơn giản như sum(theta**2) giảm theo vòng lặp.

## 7. Cạm bẫy thường gặp

Giữ seed cố định; phân biệt personal best và global best.

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/supervised_learning/particle_swarm_optimization.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
