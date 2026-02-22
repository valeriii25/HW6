"""Парсинг опыта работы из текста."""

import re
from typing import Optional

import pandas as pd


def parse_experience(text: str) -> Optional[float]:
    """Извлекает опыт работы в месяцах из текста."""
    if pd.isna(text) or not isinstance(text, str):
        return None

    text_lower = text.lower()
    total_months = 0

    years_match = re.search(r"(\d+)\s*(?:год|лет|года|year|г\.)", text_lower)
    if years_match:
        total_months += int(years_match.group(1)) * 12

    months_match = re.search(r"(\d+)\s*(?:месяц|месяцев|month|мес\.)", text_lower)
    if months_match:
        total_months += int(months_match.group(1))

    return float(total_months) if total_months > 0 else None
