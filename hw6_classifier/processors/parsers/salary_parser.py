"""Парсинг зарплаты из текста."""

import re
from typing import Optional

import pandas as pd

from hw6_classifier.config import USD_TO_RUB_RATE, EUR_TO_RUB_RATE


def parse_salary(text: str) -> Optional[float]:
    """Извлекает зарплату в рублях из текста."""
    if pd.isna(text) or not isinstance(text, str):
        return None

    text_clean = text.replace(" ", "").replace("\xa0", "").lower()

    salary_match = re.search(r"(\d+)", text_clean)
    if not salary_match:
        return None

    salary = float(salary_match.group(1))

    if "usd" in text_clean or "$" in text_clean:
        salary *= USD_TO_RUB_RATE
    elif "eur" in text_clean or "€" in text_clean:
        salary *= EUR_TO_RUB_RATE

    return salary
