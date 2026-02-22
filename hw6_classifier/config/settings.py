"""
Конфигурация проекта и настройки путей.

Модуль содержит константы путей к файлам данных, моделей и визуализаций,
а также базовые параметры для обучения моделей.
"""

from pathlib import Path
from typing import Final

# Корневая директория проекта
PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent.parent

# Директории для данных
DATA_DIR: Final[Path] = PROJECT_ROOT / "data"
RAW_DATA_DIR: Final[Path] = DATA_DIR / "raw"
PROCESSED_DATA_DIR: Final[Path] = DATA_DIR / "processed"

# Директории для моделей и артефактов
MODELS_DIR: Final[Path] = PROJECT_ROOT / "models"
METRICS_DIR: Final[Path] = PROJECT_ROOT / "metrics"
PLOTS_DIR: Final[Path] = PROJECT_ROOT / "plots"

# Параметры по умолчанию
DEFAULT_RANDOM_SEED: Final[int] = 42
DEFAULT_TEST_SIZE: Final[float] = 0.2
DEFAULT_CV_FOLDS: Final[int] = 5

# Создание необходимых директорий
for directory in [
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODELS_DIR,
    METRICS_DIR,
    PLOTS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)
