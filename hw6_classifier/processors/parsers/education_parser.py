"""Парсинг уровня образования из текста."""

from typing import Optional

import pandas as pd

from hw6_classifier.config import EDUCATION_LEVELS


def parse_education(text: str) -> Optional[int]:
    """Определяет уровень образования (0-3)."""
    if pd.isna(text) or not isinstance(text, str):
        return None

    text_lower = text.lower()

    for level_name, level_code in EDUCATION_LEVELS.items():
        if level_name in text_lower:
            return level_code

    return 3
