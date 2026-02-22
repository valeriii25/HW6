"""Классификатор на основе случайного леса."""

from sklearn.ensemble import RandomForestClassifier
from sklearn.base import BaseEstimator

from ..core import AbstractClassifier, register_classifier


@register_classifier("random_forest")
class RandomForestClassifierWrapper(AbstractClassifier):
    """
    Классификатор на основе случайного леса.

    Использует RandomForestClassifier с балансировкой классов
    для робастной классификации с оценкой важности признаков.

    Атрибуты:
        n_estimators: Количество деревьев в лесу.
        max_depth: Максимальная глубина деревьев.
        min_samples_split: Минимум образцов для разделения узла.
        max_features: Количество признаков для разделения.
    """

    def __init__(
        self,
        random_seed: int = 42,
        class_weight: str = "balanced",
        n_estimators: int = 100,
        max_depth: int | None = None,
        min_samples_split: int = 2,
        max_features: str = "sqrt",
    ) -> None:
        """Инициализирует классификатор случайного леса."""
        super().__init__(random_seed=random_seed, class_weight=class_weight)
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features

    def _create_estimator(self) -> BaseEstimator:
        """
        Создает классификатор случайного леса.

        Вернет:
            Настроенный RandomForestClassifier.
        """
        return RandomForestClassifier(
            n_estimators=self.n_estimators,
            max_depth=self.max_depth,
            min_samples_split=self.min_samples_split,
            max_features=self.max_features,
            random_state=self.random_seed,
            class_weight=self.class_weight,
            n_jobs=-1,
        )
