"""Загрузка данных из CSV."""

import logging

from hw6_classifier.processors import ResumeDataProcessor


logger = logging.getLogger(__name__)


def load_and_process_data(csv_path: str):
    """Загружает и обрабатывает данные из CSV."""
    logger.info("Этап 1: Обработка данных из CSV")
    logger.info("-" * 80)

    processor = ResumeDataProcessor()

    try:
        data = processor.process_csv(csv_path)
        logger.info("✓ Данные обработаны успешно")
        logger.info(f"  - Количество образцов: {data.n_samples}")
        logger.info(f"  - Количество признаков: {data.n_features}")
        logger.info("")
        return data
    except Exception as e:
        logger.error(f"✗ Ошибка при обработке данных: {e}")
        return None
