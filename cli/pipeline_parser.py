"""Парсер аргументов CLI для пайплайна классификации."""

import argparse

from hw6_classifier.config import DEFAULT_RANDOM_SEED, DEFAULT_TEST_SIZE, DEFAULT_CV_FOLDS


def create_parser() -> argparse.ArgumentParser:
    """Создаёт парсер аргументов командной строки."""
    parser = argparse.ArgumentParser(
        description="Пайплайн классификации уровня IT-специалистов",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("--csv", type=str, required=True, help="Путь к CSV-файлу с резюме")
    parser.add_argument("--models", type=str, nargs="+", default=["logistic", "random_forest"], help="Список моделей")
    parser.add_argument("--test-size", type=float, default=DEFAULT_TEST_SIZE, help="Доля тестовой выборки")
    parser.add_argument("--random-seed", type=int, default=DEFAULT_RANDOM_SEED, help="Зерно случайных чисел")
    parser.add_argument("--tune", action="store_true", help="Включить подбор гиперпараметров")
    parser.add_argument("--cv-folds", type=int, default=DEFAULT_CV_FOLDS, help="Количество фолдов CV")

    return parser


def parse_arguments() -> argparse.Namespace:
    """Парсит аргументы командной строки."""
    return create_parser().parse_args()
