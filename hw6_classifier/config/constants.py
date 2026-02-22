"""
Константы для обработки резюме и классификации.

Содержит словари ключевых слов, пороговые значения и названия колонок
для обработки данных резюме с hh.ru и определения уровня специалиста.
"""

from typing import Final

# Названия колонок в исходном CSV
CSV_COLUMNS: Final[dict[str, str]] = {
    "position": "Ищет работу на должность:",
    "salary": "ЗП",
    "demographics": "Пол, возраст",
    "city": "Город",
    "experience": "Опыт (двойное нажатие для полной версии)",
    "education": "Образование и ВУЗ",
}

# Ключевые слова для фильтрации IT-разработчиков
IT_DEVELOPER_KEYWORDS: Final[frozenset[str]] = frozenset(
    [
        "разработчик",
        "developer",
        "программист",
        "programmer",
        "backend",
        "frontend",
        "fullstack",
        "full stack",
        "full-stack",
        "software engineer",
        "инженер-программист",
        "веб-разработчик",
        "web developer",
        "mobile developer",
        "ios developer",
        "android developer",
        "react",
        "python",
        "java",
    ]
)

# Словарь ключевых слов для определения уровня специалиста
SENIORITY_KEYWORDS: Final[dict[str, frozenset[str]]] = {
    "junior": frozenset(
        [
            "junior",
            "младший",
            "стажёр",
            "стажер",
            "помощник",
            "ассистент",
            "trainee",
            "intern",
            "джуниор",
            "джун",
        ]
    ),
    "middle": frozenset(["middle", "миддл", "мидл"]),
    "senior": frozenset(
        [
            "senior",
            "старший",
            "ведущий",
            "синьор",
            "сеньор",
            "lead",
            "главный",
            "руководитель",
            "архитектор",
            "principal",
            "team lead",
            "тимлид",
            "сениор",
            "синьёр",
        ]
    ),
}

# Пороговые значения опыта для определения уровня (в месяцах)
JUNIOR_MAX_EXPERIENCE_MONTHS: Final[int] = 24  # До 2 лет
MIDDLE_MAX_EXPERIENCE_MONTHS: Final[int] = 60  # До 5 лет

# Технологии для извлечения признаков
TECH_STACK: Final[frozenset[str]] = frozenset(
    [
        "python",
        "java",
        "javascript",
        "typescript",
        "c++",
        "c#",
        "golang",
        "go",
        "rust",
        "php",
        "ruby",
        "swift",
        "kotlin",
        "react",
        "vue",
        "angular",
        "node.js",
        "nodejs",
        "django",
        "flask",
        "spring",
        "postgresql",
        "postgres",
        "mysql",
        "mongodb",
        "redis",
        "docker",
        "kubernetes",
        "k8s",
        "aws",
        "azure",
        "git",
        "linux",
        "1с",
        "1c",
    ]
)

# Города-миллионники России
MAJOR_CITIES: Final[frozenset[str]] = frozenset(
    [
        "москва",
        "moscow",
        "санкт-петербург",
        "петербург",
        "saint petersburg",
        "новосибирск",
        "екатеринбург",
        "казань",
        "нижний новгород",
        "челябинск",
        "самара",
        "омск",
        "ростов-на-дону",
        "уфа",
        "красноярск",
        "воронеж",
        "пермь",
        "волгоград",
    ]
)

# Уровни образования (порядковая шкала)
EDUCATION_LEVELS: Final[dict[str, int]] = {
    "среднее": 0,
    "средне-специальное": 1,
    "неполное высшее": 2,
    "высшее": 3,
    "бакалавр": 3,
    "магистр": 3,
    "специалист": 3,
}

# Целевые метки классов
TARGET_CLASSES: Final[list[str]] = ["junior", "middle", "senior"]

# Названия признаков
FEATURE_NAMES: Final[list[str]] = [
    "experience_months",
    "salary_rub",
    "age",
    "gender",
    "education_level",
    "city_million",
    "city_moscow",
    "city_spb",
]

# Название колонки целевой переменной
TARGET_COLUMN_NAME: Final[str] = "seniority_level"

# Курсы валют для конвертации зарплаты в рубли
USD_TO_RUB_RATE: Final[float] = 75.0
EUR_TO_RUB_RATE: Final[float] = 85.0
