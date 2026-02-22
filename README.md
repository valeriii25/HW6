# HW6: Классификация уровня IT-специалистов

Пайплайн для классификации резюме по уровням: junior, middle, senior.

## Описание проекта

Проект реализует полный цикл обработки и классификации:
- Загрузка и обработка CSV с резюме hh.ru
- Фильтрация IT-разработчиков
- Извлечение признаков из текстовых полей
- Обучение моделей классификации
- Оценка качества и генерация отчётов

## Системные требования

- Python 3.10+
- Операционная система: Windows / Linux / macOS

## Зависимости

```
numpy>=1.21.0
pandas>=2.0.0
scikit-learn>=1.0.0
matplotlib>=3.5.0
joblib>=1.2.0
```

## Настройка окружения

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Точка входа

- `run_pipeline.py` — главный скрипт запуска пайплайна

## Запуск

```bash
# Базовый запуск
python run_pipeline.py --csv data/resumes.csv

# С указанием моделей
python run_pipeline.py --csv data/resumes.csv --models logistic random_forest

# С подбором гиперпараметров
python run_pipeline.py --csv data/resumes.csv --tune

# Полные параметры
python run_pipeline.py --csv data/resumes.csv --models logistic svm --tune --cv-folds 5
```

## Архитектура проекта

```
HW6/
├── run_pipeline.py           # Точка входа
├── cli/                      # Парсер аргументов
├── pipeline/                 # Шаги пайплайна
│   ├── param_grids.py        # Сетки гиперпараметров
│   └── steps/                # Этапы обработки
├── hw6_classifier/           # Основной пакет
│   ├── config/               # Конфигурация и константы
│   ├── core/                 # Базовый класс и реестр
│   ├── models/               # Реализации классификаторов
│   ├── processors/           # Обработка данных
│   └── analytics/            # Визуализация и оценка
├── models/                   # Сохранённые модели
├── metrics/                  # Сохранённые метрики
├── plots/                    # Графики
└── docs/                     # Документация
```

Подробнее: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

## Доступные модели

- `logistic` — Логистическая регрессия
- `random_forest` — Случайный лес
- `gradient_boosting` — Градиентный бустинг
- `svm` — Метод опорных векторов

## Выходные данные

После выполнения создаются:
- `models/<model>_model.pkl` — обученные модели
- `metrics/<model>_metrics.json` — метрики качества
- `plots/class_distribution.png` — график распределения классов
