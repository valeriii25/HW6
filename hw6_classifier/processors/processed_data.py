"""Контейнер для обработанных данных резюме."""

from dataclasses import dataclass

import numpy as np


@dataclass
class ProcessedData:
    """
    Контейнер для обработанных данных резюме.

    Атрибуты:
        X: Матрица признаков формы (n_samples, n_features).
        y: Вектор целевых меток формы (n_samples,).
        feature_names: Список названий признаков.
        class_names: Список названий классов.
    """

    X: np.ndarray
    y: np.ndarray
    feature_names: list[str]
    class_names: list[str]

    @property
    def n_samples(self) -> int:
        """Возвращает количество образцов."""
        return self.X.shape[0]

    @property
    def n_features(self) -> int:
        """Возвращает количество признаков."""
        return self.X.shape[1]
