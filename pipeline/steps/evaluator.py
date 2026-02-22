"""Оценка моделей классификации."""

import json
import logging

from hw6_classifier.config import METRICS_DIR
from hw6_classifier.analytics import evaluate_classifier, generate_conclusion


logger = logging.getLogger(__name__)


def evaluate_single_model(model_name: str, model, x_test, y_test, class_names):
    """Оценивает одну модель и сохраняет метрики."""
    logger.info(f"Оценка модели: {model_name}")
    logger.info("-" * 80)

    y_pred = model.predict(x_test)
    metrics = evaluate_classifier(y_test, y_pred, class_names)

    logger.info("Метрики качества:")
    logger.info(f"  Accuracy:        {metrics.accuracy:.4f}")
    logger.info(f"  Precision (макро): {metrics.precision_macro:.4f}")
    logger.info(f"  Recall (макро):    {metrics.recall_macro:.4f}")
    logger.info(f"  F1-score (макро):  {metrics.f1_macro:.4f}")
    logger.info("")

    logger.info("Детальный отчёт классификации:")
    logger.info(metrics.report)
    logger.info("")

    conclusion = generate_conclusion(metrics, model_name)
    print(conclusion)

    metrics_dict = metrics.to_dict()
    metrics_dict["model_name"] = model_name

    metrics_path = METRICS_DIR / f"{model_name}_metrics.json"
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_dict, f, ensure_ascii=False, indent=2)

    logger.info(f"✓ Метрики сохранены: {metrics_path}")
    logger.info("")

    return metrics_dict


def evaluate_models(trained_models: dict, x_test, y_test, class_names):
    """Оценивает все обученные модели."""
    logger.info("Этап 5: Оценка качества моделей")
    logger.info("=" * 80)
    logger.info("")

    all_metrics = {}

    for model_name, model in trained_models.items():
        metrics_dict = evaluate_single_model(model_name, model, x_test, y_test, class_names)
        all_metrics[model_name] = metrics_dict

    return all_metrics
