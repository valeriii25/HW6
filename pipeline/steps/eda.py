"""Разведочный анализ данных."""

import logging

from hw6_classifier.config import PLOTS_DIR
from hw6_classifier.analytics import plot_class_distribution, analyze_class_balance


logger = logging.getLogger(__name__)


def perform_eda(data):
    """Выполняет разведочный анализ данных и визуализацию."""
    logger.info("Этап 2: Разведочный анализ данных (EDA)")
    logger.info("-" * 80)

    balance_info = analyze_class_balance(data.y, data.class_names)

    logger.info("Распределение классов:")
    for class_name, count in balance_info["counts"].items():
        pct = balance_info["percentages"][class_name]
        logger.info(f"  - {class_name}: {count} ({pct:.1f}%)")

    logger.info(f"  - Коэффициент дисбаланса: {balance_info['imbalance_ratio']:.2f}")
    balanced_status = "Да" if balance_info["is_balanced"] else "Нет"
    logger.info(f"  - Сбалансированность: {balanced_status}")
    logger.info("")

    plot_path = PLOTS_DIR / "class_distribution.png"
    plot_class_distribution(data.y, data.class_names, save_path=plot_path)
    logger.info("")
