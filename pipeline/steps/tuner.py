"""Подбор гиперпараметров моделей."""

import logging

from sklearn.model_selection import GridSearchCV

from pipeline.param_grids import get_param_grid


logger = logging.getLogger(__name__)


def tune_hyperparameters(classifier_class, model_name: str, x_train, y_train, args):
    """Выполняет подбор гиперпараметров модели."""
    logger.info("  Выполняется подбор гиперпараметров...")

    param_grid = get_param_grid(model_name)

    if param_grid:
        base_model = classifier_class(random_seed=args.random_seed)
        base_estimator = base_model._create_estimator()

        grid_search = GridSearchCV(
            base_estimator, param_grid, cv=args.cv_folds,
            scoring="f1_macro", n_jobs=-1, verbose=0,
        )

        grid_search.fit(x_train, y_train)

        logger.info(f"  ✓ Лучшие параметры: {grid_search.best_params_}")
        logger.info(f"  ✓ Лучший F1 (CV): {grid_search.best_score_:.4f}")

        return classifier_class(random_seed=args.random_seed, **grid_search.best_params_)
    else:
        logger.info("  ! Нет предопределенной сетки параметров, используются defaults")
        return classifier_class(random_seed=args.random_seed)
