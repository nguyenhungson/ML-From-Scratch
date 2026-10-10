# ML From Scratch — Tự implement từng module (bản thực hành)

> Bản thực hành được tạo từ ZIP repository ML-From-Scratch người dùng cung cấp. **Toàn bộ package `mlfromscratch/` và examples gốc được giữ nguyên**. Source gốc (2019) không bị xóa, ghi đè hoặc tự ý “sửa cho chạy” nhằm tránh phá mất baseline. README dự án ban đầu nằm ở `README_ORIGINAL.md`.

## Mục tiêu

Mỗi thuật toán là **một bài riêng** trong `practice/lessons/<nhóm>/<tên_module>/`, có:

- `student.py`: API/class/method theo module gốc; **toàn bộ phần implement để TODO**. Không import bất kỳ code thuật toán nào từ repo gốc hoặc bài khác.
- `README.md`: mục đích, công thức, bước thực hiện, inputs/outputs, interface, kiểm thử và lỗi thường gặp, bằng tiếng Việt.
- `HINTS.md`: các gợi ý theo tầng, không cho đáp án code.
- `tests/test_student.py`: bài test chạy độc lập cho module, gồm kiểm tra API và test hành vi/hình dạng khi có thể. Test hành vi **thất bại là bình thường** lúc chưa implement.

**Lưu ý về “độc lập”**: mỗi `student.py` độc lập *về import/source code*, chỉ cần NumPy/stdlib. Bạn vẫn nên học các thuật toán theo thứ tự nền tảng trước; các bài GAN, CNN, DQN cần tự viết rất nhiều thành phần trong cùng module. Gói này là skeleton + bài thực hành, **không phải 39 mô hình đã hoàn thiện**.

## Cài môi trường (Windows PowerShell)

```powershell
cd ML-From-Scratch-master
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-practice.txt
python practice/run.py list
python practice/verify_scaffold.py  # Kiểm tra tất cả skeleton import độc lập
```

**Linux/WSL:** dùng `source .venv/bin/activate` thay cho lệnh PowerShell.

## Cách học một module

Ví dụ K-Means:

```powershell
python practice/run.py show unsupervised_learning/k_means
# Mở practice/lessons/unsupervised_learning/k_means/student.py
# Implement từng TODO, đọc README.md và HINTS.md nếu bí
python practice/run.py test unsupervised_learning/k_means
python practice/run.py status
```

Ví dụ Logistic Regression:

```powershell
python practice/run.py show logistic_regression
python practice/run.py test logistic_regression
```

Có thể chỉ chạy unit test của bài hiện tại từ trong thư mục lesson:

```powershell
cd practice/lessons/supervised_learning/logistic_regression
python -m unittest discover -s tests -v
```

> `python practice/run.py test-all` được thiết kế để báo nhiều FAIL lúc bạn chưa hoàn thành. Đừng coi đây là lỗi setup.

## Cấu trúc

```text
ML-From-Scratch-master/
├── mlfromscratch/              # ORIGINAL — source của tác giả, KHÔNG sửa
├── README_ORIGINAL.md          # README gốc
├── requirements-practice.txt   # cài tối thiểu chỉ NumPy cho exercises
├── practice/
│   ├── run.py                  # CLI list/show/test/status/test-all
│   ├── index.json              # catalog 39 modules
│   └── lessons/
│       ├── utils/
│       ├── supervised_learning/
│       ├── unsupervised_learning/
│       ├── deep_learning/
│       └── reinforcement_learning/
└── README.md                   # hướng dẫn này
```

## Lộ trình khuyến nghị

1. **Toán/NumPy & dữ liệu**: `utils/data_operation`, `utils/data_manipulation`, `utils/kernels`.
2. **Supervised cơ bản**: `k_nearest_neighbors`, `perceptron`, `regression`, `logistic_regression`, `naive_bayes`.
3. **Unsupervised cơ bản**: `k_means`, `principal_component_analysis`, `dbscan`.
4. **Cây & ensemble**: `decision_tree`, `random_forest`, `adaboost`, `gradient_boosting`, `support_vector_machine`.
5. **Deep Learning blocks**: `activation_functions`, `loss_functions`, `optimizers`, `layers`, `neural_network`, `multilayer_perceptron`.
6. **Advanced**: GMM, LDA, Apriori, FP-Growth, Gaussian/Bayesian, XGBoost-style, PSO/GA, RBM, autoencoder, GAN/DCGAN, DQN.

**Nguyên tắc hoàn thành từng bài:** (a) code import được; (b) tất cả TODO cần thiết đã được thay; (c) test pass; (d) test ít nhất một case tự tạo; (e) giải thích được công thức và độ phức tạp; (f) cuối cùng mới mở mã `mlfromscratch/...` để đối chiếu.

## Catalog đầy đủ

| Module | Mức độ | Hàm TODO | Unit test hành vi |
|---|---|---:|---|
| [`utils/kernels`](practice/lessons/utils/kernels/README.md) | 01 Cơ sở | 3 | Có |
| [`utils/data_operation`](practice/lessons/utils/data_operation/README.md) | 01 Cơ sở | 8 | Có |
| [`utils/data_manipulation`](practice/lessons/utils/data_manipulation/README.md) | 01 Cơ sở | 12 | Có |
| [`utils/misc`](practice/lessons/utils/misc/README.md) | 02 Công cụ | 5 | API/constructor |
| [`supervised_learning/perceptron`](practice/lessons/supervised_learning/perceptron/README.md) | 02 Supervised | 3 | Có |
| [`supervised_learning/k_nearest_neighbors`](practice/lessons/supervised_learning/k_nearest_neighbors/README.md) | 02 Supervised | 3 | Có |
| [`supervised_learning/logistic_regression`](practice/lessons/supervised_learning/logistic_regression/README.md) | 02 Supervised | 4 | Có |
| [`supervised_learning/naive_bayes`](practice/lessons/supervised_learning/naive_bayes/README.md) | 02 Supervised | 5 | Có |
| [`supervised_learning/regression`](practice/lessons/supervised_learning/regression/README.md) | 03 Supervised | 28 | Có |
| [`supervised_learning/decision_tree`](practice/lessons/supervised_learning/decision_tree/README.md) | 03 Supervised | 18 | Có |
| [`supervised_learning/random_forest`](practice/lessons/supervised_learning/random_forest/README.md) | 04 Ensemble | 3 | Có |
| [`supervised_learning/adaboost`](practice/lessons/supervised_learning/adaboost/README.md) | 04 Ensemble | 5 | Có |
| [`supervised_learning/gradient_boosting`](practice/lessons/supervised_learning/gradient_boosting/README.md) | 04 Ensemble | 6 | Có |
| [`supervised_learning/support_vector_machine`](practice/lessons/supervised_learning/support_vector_machine/README.md) | 04 Supervised | 3 | Có |
| [`supervised_learning/linear_discriminant_analysis`](practice/lessons/supervised_learning/linear_discriminant_analysis/README.md) | 03 Supervised | 4 | Có |
| [`supervised_learning/multi_class_lda`](practice/lessons/supervised_learning/multi_class_lda/README.md) | 04 Supervised | 4 | Có |
| [`supervised_learning/multilayer_perceptron`](practice/lessons/supervised_learning/multilayer_perceptron/README.md) | 05 Deep Learning | 5 | Có |
| [`supervised_learning/bayesian_regression`](practice/lessons/supervised_learning/bayesian_regression/README.md) | 05 Xác suất | 4 | API/constructor |
| [`supervised_learning/xgboost`](practice/lessons/supervised_learning/xgboost/README.md) | 06 Advanced | 7 | API/constructor |
| [`supervised_learning/neuroevolution`](practice/lessons/supervised_learning/neuroevolution/README.md) | 06 Advanced | 8 | API/constructor |
| [`supervised_learning/particle_swarm_optimization`](practice/lessons/supervised_learning/particle_swarm_optimization/README.md) | 06 Advanced | 6 | API/constructor |
| [`unsupervised_learning/k_means`](practice/lessons/unsupervised_learning/k_means/README.md) | 02 Unsupervised | 7 | Có |
| [`unsupervised_learning/dbscan`](practice/lessons/unsupervised_learning/dbscan/README.md) | 03 Unsupervised | 5 | Có |
| [`unsupervised_learning/principal_component_analysis`](practice/lessons/unsupervised_learning/principal_component_analysis/README.md) | 02 Unsupervised | 1 | Có |
| [`unsupervised_learning/gaussian_mixture_model`](practice/lessons/unsupervised_learning/gaussian_mixture_model/README.md) | 04 Unsupervised | 8 | Có |
| [`unsupervised_learning/partitioning_around_medoids`](practice/lessons/unsupervised_learning/partitioning_around_medoids/README.md) | 03 Unsupervised | 8 | Có |
| [`unsupervised_learning/apriori`](practice/lessons/unsupervised_learning/apriori/README.md) | 04 Data mining | 10 | Có |
| [`unsupervised_learning/fp_growth`](practice/lessons/unsupervised_learning/fp_growth/README.md) | 05 Data mining | 12 | Có |
| [`unsupervised_learning/restricted_boltzmann_machine`](practice/lessons/unsupervised_learning/restricted_boltzmann_machine/README.md) | 06 Deep Generative | 5 | Có |
| [`unsupervised_learning/genetic_algorithm`](practice/lessons/unsupervised_learning/genetic_algorithm/README.md) | 04 Optimization | 6 | Có |
| [`unsupervised_learning/autoencoder`](practice/lessons/unsupervised_learning/autoencoder/README.md) | 06 Deep Generative | 5 | API/constructor |
| [`unsupervised_learning/generative_adversarial_network`](practice/lessons/unsupervised_learning/generative_adversarial_network/README.md) | 07 Deep Generative | 5 | API/constructor |
| [`unsupervised_learning/dcgan`](practice/lessons/unsupervised_learning/dcgan/README.md) | 07 Deep Generative | 5 | API/constructor |
| [`deep_learning/activation_functions`](practice/lessons/deep_learning/activation_functions/README.md) | 02 Deep Learning | 19 | Có |
| [`deep_learning/loss_functions`](practice/lessons/deep_learning/loss_functions/README.md) | 02 Deep Learning | 10 | Có |
| [`deep_learning/optimizers`](practice/lessons/deep_learning/optimizers/README.md) | 03 Deep Learning | 12 | Có |
| [`deep_learning/layers`](practice/lessons/deep_learning/layers/README.md) | 04 Deep Learning | 68 | Có |
| [`deep_learning/neural_network`](practice/lessons/deep_learning/neural_network/README.md) | 05 Deep Learning | 10 | API/constructor |
| [`reinforcement_learning/deep_q_network`](practice/lessons/reinforcement_learning/deep_q_network/README.md) | 07 RL | 7 | API/constructor |

## Giới hạn cần biết

- **Giữ nguyên chữ ký của source gốc**, nhưng bỏ nội dung implement và import phụ thuộc; default tham số tham chiếu object/func trong module khác được đổi thành `None` cho phép import standalone. Cần kiểm tra ý nghĩa default trong `README_ORIGINAL.md` khi tự làm.
- Module có nhiều class thì skeleton liệt kê đầy đủ, nên có thể có rất nhiều TODO (đặc biệt `layers.py`, `regression.py`). Hãy làm theo từng nhóm phương thức; không nhất thiết xong cả file trong một buổi.
- Test đi kèm chủ yếu là *minimal behavior checks*, **không xác nhận chất lượng mô hình mức nghiên cứu**; đặc biệt phần GAN/DQN và những bài nâng cao chỉ có scaffold/API/constructor test ban đầu. Hãy tự viết thêm unit tests và numerical checks.
- Package gốc dùng dependency cũ (gym, cvxopt, progressbar33...). `requirements-practice.txt` **không** cố cài toàn bộ dependencies cũ vì các bài `student.py` là độc lập. Cài `requirements.txt` cũ chỉ nếu bạn muốn chạy các examples tham khảo và phù hợp phiên bản Python.
- `README_ORIGINAL.md` có thể dẫn liên kết bên ngoài; phần thực hành không cần truy cập internet.
