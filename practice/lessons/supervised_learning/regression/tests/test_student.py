
import importlib.util
from pathlib import Path

import numpy as np
import pytest


# Load student.py independently
STUDENT_PATH = Path(__file__).resolve().parents[1] / "student.py"
spec = importlib.util.spec_from_file_location("regression_student", STUDENT_PATH)
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)


@pytest.fixture(autouse=True)
def fixed_seed():
    np.random.seed(42)


def linear_data():
    X = np.linspace(-1, 1, 40).reshape(-1, 1)
    y = 1.5 + 2 * X[:, 0]
    return X, y


def quadratic_data():
    X = np.linspace(-1, 1, 40).reshape(-1, 1)
    x = X[:, 0]
    y = 1 + 1.5 * x + 0.8 * x**2
    return X, y


def check_predictions(model, X, y, tolerance=0.05):
    pred = np.asarray(model.predict(X))
    assert pred.shape == y.shape, f"Wrong shape: {pred.shape}"
    assert np.all(np.isfinite(pred)), "Prediction contains NaN/Inf"
    mse = np.mean((pred - y) ** 2)
    assert mse < tolerance, f"MSE too high: {mse:.6f}"


# =========================================================
# 1. L1 REGULARIZATION
# =========================================================

def test_l1_penalty():
    model = student.l1_regularization(alpha=0.1)
    w = np.array([2.0, -3.0, 4.0])
    assert model(w) == pytest.approx(0.9)


def test_l1_gradient():
    model = student.l1_regularization(alpha=0.1)
    w = np.array([2.0, -3.0, 0.0])
    expected = np.array([0.1, -0.1, 0.0])
    np.testing.assert_allclose(model.grad(w), expected)


# =========================================================
# 2. L2 REGULARIZATION
# =========================================================

def test_l2_penalty():
    model = student.l2_regularization(alpha=0.1)
    w = np.array([2.0, -3.0, 4.0])
    assert model(w) == pytest.approx(2.9)


def test_l2_gradient():
    model = student.l2_regularization(alpha=0.1)
    w = np.array([2.0, -3.0, 4.0])
    expected = np.array([0.4, -0.6, 0.8])
    np.testing.assert_allclose(model.grad(w), expected)


# =========================================================
# 3. L1 + L2 REGULARIZATION
# =========================================================

def test_l1_l2_penalty():
    alpha = 0.2
    ratio = 0.3
    w = np.array([2.0, -3.0, 4.0])

    model = student.l1_l2_regularization(alpha, ratio)

    expected = alpha * (
        ratio * np.sum(np.abs(w))
        + (1 - ratio) * np.sum(w**2)
    )
    assert model(w) == pytest.approx(expected)


def test_l1_l2_gradient():
    alpha = 0.2
    ratio = 0.3
    w = np.array([2.0, -3.0, 0.0])

    model = student.l1_l2_regularization(alpha, ratio)

    expected = alpha * (
        ratio * np.sign(w)
        + 2 * (1 - ratio) * w
    )
    np.testing.assert_allclose(model.grad(w), expected)


@pytest.mark.parametrize("ratio", [0.0, 1.0])
def test_l1_l2_ratio_boundaries(ratio):
    w = np.array([2.0, -3.0])
    alpha = 0.1
    model = student.l1_l2_regularization(alpha, ratio)

    expected = (
        student.l2_regularization(alpha)(w)
        if ratio == 0.0
        else student.l1_regularization(alpha)(w)
    )
    assert model(w) == pytest.approx(expected)


# =========================================================
# 4. BASE REGRESSION
# =========================================================

def test_regression_initialize_weights():
    model = student.Regression(100, 0.01)
    model.initialize_weights(3)

    assert np.asarray(model.w).shape == (3,)
    assert np.isscalar(model.b)
    assert np.all(np.isfinite(model.w))


def test_regression_fit():
    X, y = linear_data()

    model = student.Regression(
        n_iterations=2000,
        learning_rate=0.05
    )
    model.fit(X, y)

    check_predictions(model, X, y, tolerance=0.005)


def test_regression_multiple_features():
    x = np.linspace(-1, 1, 40)
    X = np.column_stack([x, x**2])
    y = 1 + 2*x - 0.5*x**2

    model = student.Regression(3000, 0.05)
    model.fit(X, y)

    check_predictions(model, X, y, tolerance=0.005)


# =========================================================
# 5. LINEAR REGRESSION
# =========================================================

def test_linear_gradient_descent():
    X, y = linear_data()

    model = student.LinearRegression(
        n_iterations=2000,
        learning_rate=0.05,
        gradient_descent=True
    )
    model.fit(X, y)

    check_predictions(model, X, y, tolerance=0.005)


def test_linear_least_squares():
    X, y = linear_data()

    model = student.LinearRegression(
        gradient_descent=False
    )
    model.fit(X, y)

    check_predictions(model, X, y, tolerance=1e-10)
    np.testing.assert_allclose(model.w, [2.0], atol=1e-6)
    assert model.b == pytest.approx(1.5, abs=1e-6)


# =========================================================
# 6. LASSO REGRESSION
# =========================================================

def test_lasso_fit():
    X, y = quadratic_data()

    model = student.LassoRegression(
        degree=2,
        reg_factor=0.01,
        n_iterations=3000,
        learning_rate=0.03
    )
    model.fit(X, y)

    check_predictions(model, X, y, tolerance=0.05)
    assert len(model.w) == 2


def test_lasso_regularization_effect():
    X, y = linear_data()

    weak = student.LassoRegression(
        degree=1,
        reg_factor=0.0,
        n_iterations=2000,
        learning_rate=0.03
    )
    strong = student.LassoRegression(
        degree=1,
        reg_factor=0.5,
        n_iterations=2000,
        learning_rate=0.03
    )

    weak.fit(X, y)
    strong.fit(X, y)

    assert np.linalg.norm(strong.w, 1) < np.linalg.norm(weak.w, 1)


# =========================================================
# 7. POLYNOMIAL REGRESSION
# =========================================================

def test_polynomial_degree_2():
    X, y = quadratic_data()

    model = student.PolynomialRegression(
        degree=2,
        n_iterations=3000,
        learning_rate=0.03
    )
    model.fit(X, y)

    check_predictions(model, X, y, tolerance=0.01)
    assert len(model.w) == 2


def test_polynomial_predict_new_data():
    X, y = quadratic_data()

    model = student.PolynomialRegression(
        degree=2,
        n_iterations=3000,
        learning_rate=0.03
    )
    model.fit(X, y)

    X_new = np.array([[0.0], [0.5], [1.0]])
    pred = np.asarray(model.predict(X_new))

    assert pred.shape == (3,)
    assert np.all(np.isfinite(pred))


# =========================================================
# 8. RIDGE REGRESSION
# =========================================================

def test_ridge_fit():
    X, y = linear_data()

    model = student.RidgeRegression(
        reg_factor=0.01,
        n_iterations=2000,
        learning_rate=0.05
    )
    model.fit(X, y)

    check_predictions(model, X, y, tolerance=0.02)


def test_ridge_regularization_effect():
    X, y = linear_data()

    weak = student.RidgeRegression(
        reg_factor=0.0,
        n_iterations=2000,
        learning_rate=0.05
    )
    strong = student.RidgeRegression(
        reg_factor=0.5,
        n_iterations=2000,
        learning_rate=0.05
    )

    weak.fit(X, y)
    strong.fit(X, y)

    assert np.linalg.norm(strong.w) < np.linalg.norm(weak.w)


# =========================================================
# 9. POLYNOMIAL RIDGE REGRESSION
# =========================================================

@pytest.mark.parametrize("gradient_descent", [True, False])
def test_polynomial_ridge_fit(gradient_descent):
    X, y = quadratic_data()

    model = student.PolynomialRidgeRegression(
        degree=2,
        reg_factor=0.01,
        n_iterations=3000,
        learning_rate=0.03,
        gradient_descent=gradient_descent
    )
    model.fit(X, y)

    check_predictions(model, X, y, tolerance=0.05)


# =========================================================
# 10. ELASTIC NET
# =========================================================

def test_elasticnet_fit():
    X, y = quadratic_data()

    model = student.ElasticNet(
        degree=2,
        reg_factor=0.01,
        l1_ratio=0.5,
        n_iterations=3000,
        learning_rate=0.03
    )
    model.fit(X, y)

    check_predictions(model, X, y, tolerance=0.05)


def test_elasticnet_predict_new_data():
    X, y = linear_data()

    model = student.ElasticNet(
        degree=1,
        reg_factor=0.01,
        l1_ratio=0.5,
        n_iterations=2000,
        learning_rate=0.03
    )
    model.fit(X, y)

    X_new = np.array([[0.0], [0.5], [1.0]])
    pred = np.asarray(model.predict(X_new))

    assert pred.shape == (3,)
    assert np.all(np.isfinite(pred))
