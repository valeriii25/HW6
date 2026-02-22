"""
Реестр классификаторов с декоратором для регистрации.

Модуль реализует паттерн Singleton для централизованного управления
доступными моделями классификации.
"""

from typing import Optional, Type, Dict
from .base_classifier import AbstractClassifier


class ClassifierRegistry:
    """
    Singleton-реестр для регистрации и получения классификаторов.

    Обеспечивает централизованное хранилище классов классификаторов
    и предоставляет удобный интерфейс для их получения по имени.

    Атрибуты:
        _instance: Единственный экземпляр реестра (Singleton).
        _registry: Словарь зарегистрированных классов классификаторов.
    """

    _instance: Optional["ClassifierRegistry"] = None
    _registry: Dict[str, Type[AbstractClassifier]] = {}

    def __new__(cls) -> "ClassifierRegistry":
        """
        Создает или возвращает существующий экземпляр реестра.

        Реализует паттерн Singleton, гарантируя единственность экземпляра.

        Вернет:
            Единственный экземпляр реестра.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def register(self, name: str, classifier_class: Type[AbstractClassifier]) -> None:
        """
        Регистрирует класс классификатора под заданным именем.

        Аргументы:
            name: Уникальное имя для регистрации классификатора.
            classifier_class: Класс классификатора для регистрации.

        Исключения:
            ValueError: Если имя уже зарегистрировано.
            TypeError: Если classifier_class не является подклассом AbstractClassifier.
        """
        if name in self._registry:
            raise ValueError(f"Классификатор с именем '{name}' уже зарегистрирован")

        if not issubclass(classifier_class, AbstractClassifier):
            raise TypeError(
                f"Класс {classifier_class.__name__} должен наследовать AbstractClassifier"
            )

        self._registry[name] = classifier_class

    def get(self, name: str) -> Type[AbstractClassifier]:
        """
        Возвращает класс классификатора по имени.

        Аргументы:
            name: Имя зарегистрированного классификатора.

        Вернет:
            Класс зарегистрированного классификатора.

        Исключения:
            KeyError: Если классификатор с таким именем не найден.
        """
        if name not in self._registry:
            available = ", ".join(self._registry.keys())
            raise KeyError(
                f"Классификатор '{name}' не найден. "
                f"Доступные классификаторы: {available}"
            )

        return self._registry[name]

    def list_available(self) -> list[str]:
        """
        Возвращает список имен всех зарегистрированных классификаторов.

        Вернет:
            Список имен доступных классификаторов.
        """
        return list(self._registry.keys())

    def is_registered(self, name: str) -> bool:
        """
        Проверяет, зарегистрирован ли классификатор с данным именем.

        Аргументы:
            name: Имя классификатора для проверки.

        Вернет:
            True, если классификатор зарегистрирован, иначе False.
        """
        return name in self._registry


registry = ClassifierRegistry()


def register_classifier(name: str):
    """
    Декоратор для регистрации класса классификатора в реестре.

    Использование:
        @register_classifier("logistic")
        class LogisticClassifier(AbstractClassifier):
            ...

    Аргументы:
        name: Уникальное имя для регистрации классификатора.

    Вернет:
        Функция-декоратор, регистрирующая класс.
    """

    def decorator(
        classifier_class: Type[AbstractClassifier],
    ) -> Type[AbstractClassifier]:
        """
        Внутренний декоратор для регистрации класса.

        Аргументы:
            classifier_class: Класс классификатора для регистрации.

        Вернет:
            Исходный класс (для поддержки chaining).
        """
        registry.register(name, classifier_class)
        return classifier_class

    return decorator
