# Deep Q-Network (DQN)

**Module ID:** `reinforcement_learning/deep_q_network`  
**Mức độ:** 07 RL  
**Mục tiêu:** Huấn luyện Q network trong môi trường rời rạc bằng replay buffer.

## 1. Kiến thức toán học cần hiểu

y=r+γ(1−done)max_a′Q_target(s′,a′); L=(Q(s,a)−y)².

## 2. Đầu vào / đầu ra

train(n_epochs,batch_size); set_model(model); play(n_epochs) API gốc.

## 3. Từng bước tự implement

1. **Bước 1:** Tạo replay buffer (s,a,r,s_next,done).
2. **Bước 2:** Chọn action epsilon-greedy.
3. **Bước 3:** Lấy random minibatches và build Bellman targets.
4. **Bước 4:** Huấn luyện mạng online và cập nhật target network.
5. **Bước 5:** Theo dõi episode rewards, seed, epsilon decay.

## 4. Hợp đồng code gốc (những hàm bạn tự viết)

Đây là các class/hàm của module `mlfromscratch/reinforcement_learning/deep_q_network.py`. Tập tin `student.py` chỉ giữ **tên, tham số, skeleton, TODO**, không chứa thuật toán đã giải. Nếu default của source gốc phụ thuộc class/module khác, ở skeleton được đổi thành `None` để file có thể import độc lập.

- `DeepQNetwork.__init__(self, env_name='CartPole-v1', epsilon=1, gamma=0.9, decay_rate=0.005, min_epsilon=0.1)`: Khởi tạo cấu hình/trạng thái (hyperparameters).
- `DeepQNetwork.set_model(self, model)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `DeepQNetwork._select_action(self, state)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `DeepQNetwork._memorize(self, state, action, reward, new_state, done)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `DeepQNetwork._construct_training_set(self, replay)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.
- `DeepQNetwork.train(self, n_epochs=500, batch_size=32)`: Triển khai vòng lặp huấn luyện.
- `DeepQNetwork.play(self, n_epochs)`: Tự nghiên cứu vai trò qua tên hàm và source gốc; xác định inputs/outputs.

## 5. Chạy độc lập

Chạy từ thư mục gốc project:

```bash
python practice/run.py show reinforcement_learning/deep_q_network
python practice/run.py test reinforcement_learning/deep_q_network
```

Hoặc chuyển vào thư mục này:

```bash
python -m unittest discover -s tests -v
```

**Lưu ý:** Trước khi thực hiện các `TODO`, bài test hành vi dự kiến **FAIL / ERROR**. Bạn cần làm cho test xanh. Bạn được phép bổ sung helper function trong chính `student.py` nhưng **không** được import từ `mlfromscratch` hoặc lesson khác.

## 6. Các bài tự kiểm tra

Trên mock environment kiểm thử Bellman target và replay buffer.

## 7. Cạm bẫy thường gặp

Gym API hiện đại reset()→(obs,info), step()→(obs,reward,terminated,truncated,info).

## 8. Khi bí hoặc làm xong

- Đọc `HINTS.md` (gợi ý theo tầng, không có source đáp án).
- Khi đã thử và pass test, đối chiếu **mã nguồn gốc không chỉnh sửa** tại `mlfromscratch/reinforcement_learning/deep_q_network.py`.
- So sánh tư duy thuật toán, không yêu cầu tái tạo từng dòng code gốc.
- Test đi kèm là kiểm tra tối thiểu, không thay thế benchmark, kiểm thử dữ liệu biên hay kiểm chứng gradient.
