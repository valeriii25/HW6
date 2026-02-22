"""Обучение моделей классификации."""

import logging
from pathlib import Path

import joblib

from hw6_classifier.config import MODELS_DIR
from hw6_classifier.core import registry
from pipeline.steps.tuner import tune_hyperparameters


logger = logging.getLogger(__name__)


def train_single_model(model_name: str, x_train, y_train, args):
    """Обучает одну модель классификации."""
    logger.info(f"Обучение модели: {model_name}")
    logger.info("-" * 40)

    try:
        classifier_class = registry.get(model_name)

        if args.tune:
            model = tune_hyperparameters(classifier_class, model_name, x_train, y_train, args)
        else:
            model = classifier_class(random_seed=args.random_seed)

        model.fit(x_train, y_train)

        logger.info("  ✓ Модель обучена успешно")
        logger.info("")

        model_path = MODELS_DIR / f"{model_name}_model.pkl"
        joblib.dump(model, model_path)
        logger.info(f"  ✓ Модель сохранена: {model_path}")
        logger.info("")

        return model

    except Exception as e:
        logger.error(f"  ✗ Ошибка при обучении модели {model_name}: {e}")
        logger.info("")
        return None


def train_models(model_names: list, x_train, y_train, args):
    """Обучает все указанные модели."""
    logger.info("Этап 4: Обучение моделей классификации")
    logger.info("-" * 80)
    logger.info(f"Модели для обучения: {', '.join(model_names)}")
    tuning_status = "Включен" if args.tune else "Выключен"
    logger.info(f"Подбор гиперпараметров: {tuning_status}")
    logger.info("")

    trained_models = {}

    for model_name in model_names:
        model = train_single_model(model_name, x_train, y_train, args)
        if model is not None:
            trained_models[model_name] = model

    return trained_models
