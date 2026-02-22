#!/usr/bin/env python3
"""
Главный скрипт для запуска полного пайплайна классификации резюме.

Примеры:
    python run_pipeline.py --csv data/resumes.csv
    python run_pipeline.py --csv data/resumes.csv --models logistic random_forest
    python run_pipeline.py --csv data/resumes.csv --tune
"""

import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from hw6_classifier.config import MODELS_DIR, METRICS_DIR, PLOTS_DIR
from hw6_classifier.models import gradient_boosting, logistic, random_forest, svm
from cli import parse_arguments
from pipeline import (
    load_and_process_data,
    perform_eda,
    split_dataset,
    train_models,
    evaluate_models,
    print_summary,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Главная функция пайплайна классификации."""
    args = parse_arguments()

    logger.info("=" * 80)
    logger.info("ПАЙПЛАЙН КЛАССИФИКАЦИИ УРОВНЯ IT-СПЕЦИАЛИСТОВ")
    logger.info("=" * 80)
    logger.info("")

    data = load_and_process_data(args.csv)
    if data is None:
        return

    perform_eda(data)

    x_train, x_test, y_train, y_test = split_dataset(data, args.test_size, args.random_seed)

    trained_models = train_models(args.models, x_train, y_train, args)

    all_metrics = evaluate_models(trained_models, x_test, y_test, data.class_names)

    print_summary(trained_models, all_metrics)


if __name__ == "__main__":
    main()
