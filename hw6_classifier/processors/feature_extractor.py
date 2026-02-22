"""Извлечение признаков из резюме."""

from typing import Optional

import pandas as pd

from hw6_classifier.config import (
    CSV_COLUMNS,
    TECH_STACK,
    JUNIOR_MAX_EXPERIENCE_MONTHS,
    MIDDLE_MAX_EXPERIENCE_MONTHS,
    SENIORITY_KEYWORDS,
    TARGET_COLUMN_NAME,
)
from .parsers import (
    parse_experience,
    parse_salary,
    parse_demographics,
    parse_education,
    parse_city,
    extract_tech_skills,
)


def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    """Извлекает признаки из резюме."""
    features = {}

    features["experience_months"] = df[CSV_COLUMNS["experience"]].apply(parse_experience)
    features["salary_rub"] = df[CSV_COLUMNS["salary"]].apply(parse_salary)

    demographics = df[CSV_COLUMNS["demographics"]].apply(parse_demographics)
    features["age"] = demographics.apply(lambda x: x[0])
    features["gender"] = demographics.apply(lambda x: x[1])

    features["education_level"] = df[CSV_COLUMNS["education"]].apply(parse_education)

    city_features = df[CSV_COLUMNS["city"]].apply(parse_city)
    features["city_million"] = city_features.apply(lambda x: x[0])
    features["city_moscow"] = city_features.apply(lambda x: x[1])
    features["city_spb"] = city_features.apply(lambda x: x[2])

    tech_features = df[CSV_COLUMNS["position"]].apply(extract_tech_skills)
    for tech in sorted(TECH_STACK):
        features[f"skill_{tech}"] = tech_features.apply(lambda x: int(tech in x))

    return pd.DataFrame(features)


def create_target(df: pd.DataFrame) -> pd.Series:
    """Создает целевую переменную (junior/middle/senior)."""
    position_col = CSV_COLUMNS["position"]
    experience_col = CSV_COLUMNS["experience"]

    positions_lower = df[position_col].fillna("").str.lower()

    def label_seniority(row_idx: int) -> Optional[str]:
        position = positions_lower.iloc[row_idx]

        for level, keywords in SENIORITY_KEYWORDS.items():
            if any(keyword in position for keyword in keywords):
                return level

        experience_text = df[experience_col].iloc[row_idx]
        experience_months = parse_experience(experience_text)

        if pd.isna(experience_months):
            return None

        if experience_months < JUNIOR_MAX_EXPERIENCE_MONTHS:
            return "junior"
        elif experience_months < MIDDLE_MAX_EXPERIENCE_MONTHS:
            return "middle"
        else:
            return "senior"

    return pd.Series(
        [label_seniority(i) for i in range(len(df))],
        index=df.index,
        name=TARGET_COLUMN_NAME,
    )
