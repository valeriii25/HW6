"""Классификатор на основе метода опорных векторов."""

from sklearn.svm import LinearSVC
from sklearn.base import BaseEstimator

from ..core import AbstractClassifier, register_classifier


@register_classifier("svm")
class SVMClassifier(AbstractClassifier):
    """
    Классификатор на основе метода опорных векторов.

    Использует LinearSVC для эффективной линейной классификации
    с балансировкой классов.

    Атрибуты:
        c_param: Параметр регуляризации.
        max_iter: Максимальное число итераций.
    """

    def __init__(
        self,
        random_seed: int = 42,
        class_weight: str = "balanced",
        c_param: float = 1.0,
        max_iter: int = 5000,
    ) -> None:
        """Инициализирует SVM-классификатор."""
        super().__init__(random_seed=random_seed, class_weight=class_weight)
        self.c_param = c_param
        self.max_iter = max_iter

    def _create_estimator(self) -> BaseEstimator:
        """
        Создает линейный SVM-классификатор.

        Вернет:
            Настроенный LinearSVC.
        """
        return LinearSVC(
            C=self.c_param,
            max_iter=self.max_iter,
            random_state=self.random_seed,
            class_weight=self.class_weight,
            dual="auto",
        )
