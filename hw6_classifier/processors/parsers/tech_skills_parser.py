"""Извлечение технологических навыков из текста."""

import pandas as pd

from hw6_classifier.config import TECH_STACK


def extract_tech_skills(text: str) -> set[str]:
    """Извлекает упоминания технологий из текста."""
    if pd.isna(text) or not isinstance(text, str):
        return set()

    text_lower = text.lower()
    found_skills = set()

    for tech in TECH_STACK:
        if tech.lower() in text_lower:
            found_skills.add(tech)

    return found_skills
