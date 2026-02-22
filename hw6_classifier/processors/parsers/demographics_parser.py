"""Парсинг демографических данных из текста."""

import re
from typing import Optional, Tuple

import pandas as pd


def parse_demographics(text: str) -> Tuple[Optional[int], Optional[int]]:
    """
    Извлекает возраст и пол из текста.
    
    Вернет:
        Кортеж (возраст, пол). Пол: 1 = мужчина, 0 = женщина.
    """
    if pd.isna(text) or not isinstance(text, str):
        return (None, None)

    text_lower = text.lower()

    age_match = re.search(r"(\d+)\s*(?:год|лет|года|year)", text_lower)
    age = int(age_match.group(1)) if age_match else None

    gender = None
    if "мужчина" in text_lower or "муж" in text_lower or "male" in text_lower:
        gender = 1
    elif "женщина" in text_lower or "жен" in text_lower or "female" in text_lower:
        gender = 0

    return (age, gender)
