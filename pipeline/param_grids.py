"""Сетки гиперпараметров для моделей."""

PARAM_GRIDS = {
    "logistic": {"C": [0.01, 0.1, 1.0, 10.0], "max_iter": [1000, 2000]},
    "random_forest": {
        "n_estimators": [50, 100, 200],
        "max_depth": [5, 10, None],
        "min_samples_split": [2, 5],
    },
    "gradient_boosting": {
        "n_estimators": [50, 100, 200],
        "learning_rate": [0.01, 0.1, 0.2],
        "max_depth": [3, 5],
    },
    "svm": {"C": [0.01, 0.1, 1.0, 10.0], "max_iter": [2000, 5000]},
}


def get_param_grid(model_name: str) -> dict:
    """Возвращает сетку параметров для модели."""
    return PARAM_GRIDS.get(model_name, {})
