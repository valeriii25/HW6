"""Разделение данных на train/test."""

import logging

from sklearn.model_selection import train_test_split


logger = logging.getLogger(__name__)


def split_dataset(data, test_size: float, random_seed: int):
    """Разделяет данные на тренировочную и тестовую выборки."""
    logger.info("Этап 3: Разделение на тренировочную и тестовую выборки")
    logger.info("-" * 80)

    x_train, x_test, y_train, y_test = train_test_split(
        data.X, data.y, test_size=test_size, random_state=random_seed, stratify=data.y,
    )

    logger.info("✓ Данные разделены")
    logger.info(f"  - Тренировочная выборка: {x_train.shape[0]} образцов")
    logger.info(f"  - Тестовая выборка: {x_test.shape[0]} образцов")
    logger.info("")

    return x_train, x_test, y_train, y_test
