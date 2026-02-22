# Архитектура HW6

## Структура проекта

```
HW6/
├── run_pipeline.py           # Точка входа пайплайна
├── cli/                      # CLI модули
│   └── pipeline_parser.py    # Парсер аргументов
├── pipeline/                 # Пайплайн классификации
│   ├── param_grids.py        # Сетки гиперпараметров
│   ├── steps/                # Шаги пайплайна
│   │   ├── data_loader.py    # Загрузка данных
│   │   ├── eda.py            # Разведочный анализ
│   │   ├── splitter.py       # Разделение данных
│   │   ├── tuner.py          # Подбор гиперпараметров
│   │   ├── trainer.py        # Обучение моделей
│   │   ├── evaluator.py      # Оценка моделей
│   │   └── summary.py        # Вывод результатов
│   └── __init__.py
├── hw6_classifier/           # Основной пакет классификации
│   ├── config/               # Конфигурация
│   │   ├── settings.py       # Пути и настройки
│   │   └── constants.py      # Ключевые слова и пороги
│   ├── core/                 # Ядро классификации
│   │   ├── base_classifier.py # Базовый классификатор
│   │   └── registry.py       # Реестр моделей
│   ├── models/               # Реализации моделей
│   │   ├── logistic.py
│   │   ├── random_forest.py
│   │   ├── gradient_boosting.py
│   │   └── svm.py
│   ├── processors/           # Обработка данных
│   │   ├── processed_data.py # Контейнер данных
│   │   ├── data_processor.py # Главный процессор
│   │   ├── feature_extractor.py # Извлечение признаков
│   │   └── parsers/          # Парсеры данных
│   │       ├── experience_parser.py
│   │       ├── salary_parser.py
│   │       ├── demographics_parser.py
│   │       ├── education_parser.py
│   │       ├── city_parser.py
│   │       └── tech_skills_parser.py
│   └── analytics/            # Аналитика
│       ├── visualizer.py     # Визуализация
│       └── evaluator.py      # Оценка классификации
├── models/                   # Сохранённые модели
├── metrics/                  # Сохранённые метрики
├── plots/                    # Графики
├── docs/                     # Документация
├── README.md
└── requirements.txt
```

## Пайплайн классификации

1. **Загрузка данных** — чтение CSV с резюме
2. **EDA** — анализ баланса классов, визуализация
3. **Разделение** — train/test split с стратификацией
4. **Обучение** — обучение выбранных моделей
5. **Оценка** — вычисление метрик, генерация отчётов

## Принципы проектирования

- **SRP**: Каждый шаг пайплайна в отдельном файле
- **KISS**: Минимум абстракций, понятный код
- **DRY**: Парсеры переиспользуются в разных местах
