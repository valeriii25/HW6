"""Парсинг географических признаков города."""

from typing import Tuple

import pandas as pd

from hw6_classifier.config import MAJOR_CITIES


def parse_city(text: str) -> Tuple[int, int, int]:
    """
    Определяет географические признаки города.
    
    Вернет:
        Кортеж (город-миллионник, Москва, СПб).
    """
    if pd.isna(text) or not isinstance(text, str):
        return (0, 0, 0)

    text_lower = text.lower()

    is_moscow = int("москва" in text_lower or "moscow" in text_lower)
    is_spb = int(
        "санкт-петербург" in text_lower
        or "петербург" in text_lower
        or "saint petersburg" in text_lower
    )

    is_major_city = int(any(city in text_lower for city in MAJOR_CITIES))

    return (is_major_city, is_moscow, is_spb)
