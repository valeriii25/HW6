"""
Модуль оценки качества классификаторов.

Содержит функции для вычисления метрик и генерации отчетов
о производительности моделей классификации.
"""

from dataclasses import dataclass
from typing import Dict
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)


@dataclass
class ClassificationMetrics:
    """
    Контейнер для метрик классификации.

    Атрибуты:
        accuracy: Точность (доля правильных предсказаний).
        precision_macro: Макро-усреднённая точность.
        recall_macro: Макро-усреднённый отзыв.
        f1_macro: Макро-усреднённая F1-мера.
        report: Детальный отчёт классификации (строка).
    """

    accuracy: float
    precision_macro: float
    recall_macro: float
    f1_macro: float
    report: str

    def to_dict(self) -> Dict[str, float | str]:
        """
        Преобразует метрики в словарь.

        Вернет:
            Словарь с метриками.
        """
        return {
            "accuracy": self.accuracy,
            "precision_macro": self.precision_macro,
            "recall_macro": self.recall_macro,
            "f1_macro": self.f1_macro,
            "classification_report": self.report,
        }


def evaluate_classifier(
    y_true: np.ndarray, y_pred: np.ndarray, class_names: list[str]
) -> ClassificationMetrics:
    """
    Вычисляет метрики качества классификации.

    Аргументы:
        y_true: Истинные метки классов.
        y_pred: Предсказанные метки классов.
        class_names: Список названий классов.

    Вернет:
        Контейнер с метриками классификации.
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average="macro", zero_division=0)
    recall = recall_score(y_true, y_pred, average="macro", zero_division=0)
    f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)

    report = classification_report(
        y_true, y_pred, target_names=class_names, zero_division=0
    )

    return ClassificationMetrics(
        accuracy=accuracy,
        precision_macro=precision,
        recall_macro=recall,
        f1_macro=f1,
        report=report,
    )


def generate_conclusion(
    metrics: ClassificationMetrics, model_name: str
) -> str:
    """
    Генерирует текстовое заключение о качестве модели.

    Анализирует метрики и формулирует выводы о жизнеспособности модели,
    потенциальных источниках ошибок и рекомендациях по улучшению.

    Аргументы:
        metrics: Метрики классификации.
        model_name: Название модели.

    Вернет:
        Текстовое заключение с анализом модели.
    """
    lines = []
    lines.append("=" * 80)
    lines.append(f"ЗАКЛЮЧЕНИЕ ПО МОДЕЛИ: {model_name}")
    lines.append("=" * 80)
    lines.append("")

    lines.append("1. ОБЩАЯ ОЦЕНКА КАЧЕСТВА МОДЕЛИ")
    lines.append("-" * 80)
    lines.append(
        f"   Accuracy (точность):     {metrics.accuracy:.4f} ({metrics.accuracy * 100:.2f}%)"
    )
    lines.append(f"   F1-score (макро):        {metrics.f1_macro:.4f}")
    lines.append(f"   Precision (макро):       {metrics.precision_macro:.4f}")
    lines.append(f"   Recall (макро):          {metrics.recall_macro:.4f}")
    lines.append("")

    lines.append("2. ЖИЗНЕСПОСОБНОСТЬ МОДЕЛИ")
    lines.append("-" * 80)

    if metrics.f1_macro >= 0.75:
        viability = "ВЫСОКАЯ"
        comment = "Модель показывает отличные результаты и готова к продакшену."
    elif metrics.f1_macro >= 0.60:
        viability = "СРЕДНЯЯ"
        comment = "Модель работает приемлемо, но требует дополнительной настройки."
    else:
        viability = "НИЗКАЯ"
        comment = "Модель требует существенных улучшений перед использованием."

    lines.append(f"   Оценка: {viability}")
    lines.append(f"   Комментарий: {comment}")

    lines.append("")
    lines.append("=" * 80)
    lines.append("")

    return "\n".join(lines)
