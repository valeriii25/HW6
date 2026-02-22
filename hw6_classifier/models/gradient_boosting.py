"""Классификатор на основе градиентного бустинга."""

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.base import BaseEstimator

from ..core import AbstractClassifier, register_classifier


@register_classifier("gradient_boosting")
class GradientBoostingClassifierWrapper(AbstractClassifier):
    """
    Классификатор на основе градиентного бустинга.

    Использует GradientBoostingClassifier для последовательного
    построения ансамбля слабых классификаторов.

    Атрибуты:
        n_estimators: Количество этапов бустинга.
        learning_rate: Скорость обучения.
        max_depth: Максимальная глубина деревьев.
    """

    def __init__(
        self,
        random_seed: int = 42,
        n_estimators: int = 100,
        learning_rate: float = 0.1,
        max_depth: int = 3,
    ) -> None:
        """Инициализирует классификатор градиентного бустинга."""
        super().__init__(random_seed=random_seed)
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth

    def _create_estimator(self) -> BaseEstimator:
        """
        Создает классификатор градиентного бустинга.

        Вернет:
            Настроенный GradientBoostingClassifier.
        """
        return GradientBoostingClassifier(
            n_estimators=self.n_estimators,
            learning_rate=self.learning_rate,
            max_depth=self.max_depth,
            random_state=self.random_seed,
        )
