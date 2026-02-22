"""Вывод итоговой сводки результатов."""

import logging


logger = logging.getLogger(__name__)


def print_summary(trained_models: dict, all_metrics: dict):
    """Выводит итоговую сводку результатов."""
    logger.info("=" * 80)
    logger.info("ИТОГОВАЯ СВОДКА")
    logger.info("=" * 80)
    logger.info("")
    logger.info(f"Обучено моделей: {len(trained_models)}")
    logger.info("Рейтинг моделей по F1-score (макро):")
    logger.info("")

    sorted_models = sorted(
        trained_models.items(),
        key=lambda x: all_metrics[x[0]]["f1_macro"],
        reverse=True,
    )

    for rank, (model_name, _) in enumerate(sorted_models, 1):
        f1 = all_metrics[model_name]["f1_macro"]
        acc = all_metrics[model_name]["accuracy"]
        logger.info(f"  {rank}. {model_name:20s} - F1: {f1:.4f}, Accuracy: {acc:.4f}")

    logger.info("")
    logger.info("=" * 80)
    logger.info("ПАЙПЛАЙН ЗАВЕРШЁН УСПЕШНО")
    logger.info("=" * 80)
