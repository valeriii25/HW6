"""Классификатор на основе логистической регрессии."""

from sklearn.linear_model import LogisticRegression
from sklearn.base import BaseEstimator

from ..core import AbstractClassifier, register_classifier


@register_classifier("logistic")
class LogisticClassifier(AbstractClassifier):
    """
    Классификатор на основе логистической регрессии.

    Использует LogisticRegression с балансировкой классов
    для решения задачи многоклассовой классификации.

    Атрибуты:
        c_param: Параметр регуляризации.
        max_iter: Максимальное число итераций.
    """

    def __init__(
        self,
        random_seed: int = 42,
        class_weight: str = "balanced",
        c_param: float = 1.0,
        max_iter: int = 1000,
    ) -> None:
        """Инициализирует логистический классификатор."""
        super().__init__(random_seed=random_seed, class_weight=class_weight)
        self.c_param = c_param
        self.max_iter = max_iter

    def _create_estimator(self) -> BaseEstimator:
        """
        Создает логистический регрессор.

        Вернет:
            Настроенный LogisticRegression.
        """
        return LogisticRegression(
            C=self.c_param,
            max_iter=self.max_iter,
            random_state=self.random_seed,
            class_weight=self.class_weight,
            solver="lbfgs",
        )
