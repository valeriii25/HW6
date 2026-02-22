"""Процессор данных резюме для классификации уровня специалиста."""

import numpy as np
import pandas as pd

from hw6_classifier.config import (
    CSV_COLUMNS,
    IT_DEVELOPER_KEYWORDS,
    FEATURE_NAMES,
    TARGET_COLUMN_NAME,
)
from .processed_data import ProcessedData
from .feature_extractor import extract_features, create_target


class ResumeDataProcessor:
    """
    Процессор для обработки данных резюме с hh.ru.

    Выполняет полный цикл обработки данных: загрузку из CSV,
    фильтрацию IT-разработчиков, извлечение признаков и создание
    целевой переменной (junior/middle/senior).
    """

    def __init__(self) -> None:
        """Инициализирует процессор данных."""
        from hw6_classifier.config import TECH_STACK
        self._tech_skills: list[str] = [f"skill_{tech}" for tech in sorted(TECH_STACK)]

    def process_csv(self, csv_path: str) -> ProcessedData:
        """Обрабатывает CSV-файл с резюме и возвращает готовые данные."""
        df = pd.read_csv(csv_path)

        df = self._filter_it_developers(df)

        if len(df) == 0:
            raise ValueError("После фильтрации не осталось IT-разработчиков")

        features_df = extract_features(df)
        y_series = create_target(df)

        combined_df = pd.concat([features_df, y_series], axis=1)
        combined_df = combined_df.dropna()

        if len(combined_df) < 10:
            raise ValueError(f"Недостаточно данных после обработки: {len(combined_df)} образцов")

        y = combined_df[TARGET_COLUMN_NAME].values
        X = combined_df.drop(TARGET_COLUMN_NAME, axis=1).values

        all_feature_names = list(FEATURE_NAMES) + self._tech_skills

        class_names = ["junior", "middle", "senior"]
        class_to_idx = {name: idx for idx, name in enumerate(class_names)}
        y_encoded = np.array([class_to_idx[label] for label in y])

        return ProcessedData(
            X=X, y=y_encoded, feature_names=all_feature_names, class_names=class_names,
        )

    def _filter_it_developers(self, df: pd.DataFrame) -> pd.DataFrame:
        """Фильтрует резюме IT-разработчиков."""
        position_col = CSV_COLUMNS["position"]

        if position_col not in df.columns:
            raise ValueError(f"Колонка '{position_col}' не найдена в данных")

        positions_lower = df[position_col].fillna("").str.lower()

        mask = positions_lower.apply(
            lambda pos: any(keyword in pos for keyword in IT_DEVELOPER_KEYWORDS)
        )

        return df[mask].copy()
