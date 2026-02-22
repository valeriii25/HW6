"""
Базовый абстрактный класс для всех классификаторов.

Модуль содержит абстрактный класс AbstractClassifier, реализующий
паттерн Template Method для всех моделей классификации уровня специалиста.
"""

from abc import ABC, abstractmethod
from typing import Optional
import numpy as np
from sklearn.base import BaseEstimator


class AbstractClassifier(ABC):
    """
    Базовый абстрактный класс для всех классификаторов.

    Реализует паттерн Template Method, определяя общий интерфейс для обучения
    и предсказания. Конкретные реализации должны определить метод создания
    конкретного sklearn-эстиматора.

    Атрибуты:
        random_seed: Зерно для генератора случайных чисел.
        class_weight: Стратегия балансировки классов.
        _estimator: Внутренний sklearn-эстиматор.
        _is_fitted: Флаг, указывающий, обучена ли модель.
    """

    def __init__(
        self, random_seed: int = 42, class_weight: Optional[str] = "balanced"
    ) -> None:
        """
        Инициализирует классификатор с заданными параметрами.

        Аргументы:
            random_seed: Зерно для генератора случайных чисел.
            class_weight: Стратегия балансировки классов.
        """
        self.random_seed = random_seed
        self.class_weight = class_weight
        self._estimator: Optional[BaseEstimator] = None
        self._is_fitted: bool = False

    @abstractmethod
    def _create_estimator(self) -> BaseEstimator:
        """
        Создает конкретный sklearn-эстиматор.

        Абстрактный метод, который должен быть реализован в подклассах
        для создания специфичного классификатора.

        Вернет:
            Инициализированный sklearn-эстиматор.
        """
        pass

    def fit(self, x: np.ndarray, y: np.ndarray) -> "AbstractClassifier":
        """
        Обучает классификатор на тренировочных данных.

        Создает эстиматор, валидирует данные и обучает модель.

        Аргументы:
            x: Матрица признаков формы (n_samples, n_features).
            y: Вектор целевых меток формы (n_samples,).

        Исключения:
            ValueError: Если размерности не совпадают.

        Вернет:
            Ссылка на себя для поддержки method chaining.
        """
        self._validate_dimensions(x, y)

        if self._estimator is None:
            self._estimator = self._create_estimator()

        self._estimator.fit(x, y)
        self._is_fitted = True
        return self

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        Делает предсказания для новых данных.

        Аргументы:
            x: Матрица признаков формы (n_samples, n_features).

        Исключения:
            RuntimeError: Если модель не была обучена.

        Вернет:
            Массив предсказанных меток.
        """
        self._ensure_fitted()
        return self._estimator.predict(x)

    def predict_proba(self, x: np.ndarray) -> np.ndarray:
        """
        Возвращает вероятности принадлежности к каждому классу.

        Аргументы:
            x: Матрица признаков формы (n_samples, n_features).

        Исключения:
            RuntimeError: Если модель не была обучена.
            AttributeError: Если модель не поддерживает predict_proba.

        Вернет:
            Матрица вероятностей.
        """
        self._ensure_fitted()
        self._validate_predict_proba_support()
        return self._estimator.predict_proba(x)

    def is_fitted(self) -> bool:
        """
        Проверяет, обучена ли модель.

        Вернет:
            True, если модель обучена, иначе False.
        """
        return self._is_fitted

    def get_estimator(self) -> Optional[BaseEstimator]:
        """
        Возвращает внутренний sklearn-эстиматор.

        Вернет:
            Эстиматор или None, если не создан.
        """
        return self._estimator

    @property
    def model_name(self) -> str:
        """
        Возвращает название модели.

        Вернет:
            Название класса модели.
        """
        return self.__class__.__name__

    def _validate_dimensions(self, x: np.ndarray, y: np.ndarray) -> None:
        """Проверяет соответствие размерностей матриц."""
        if x.shape[0] != y.shape[0]:
            raise ValueError(
                f"Несоответствие размерностей: x имеет {x.shape[0]} образцов, "
                f"y имеет {y.shape[0]} образцов"
            )

    def _ensure_fitted(self) -> None:
        """Проверяет, что модель обучена."""
        if not self._is_fitted:
            raise RuntimeError(
                "Модель не обучена. Вызовите метод fit() перед предсказанием."
            )

    def _validate_predict_proba_support(self) -> None:
        """Проверяет наличие метода predict_proba."""
        if not hasattr(self._estimator, "predict_proba"):
            model_type = type(self._estimator).__name__
            raise AttributeError(f"Модель {model_type} не поддерживает predict_proba")
