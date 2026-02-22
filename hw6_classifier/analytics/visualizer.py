"""
Модуль визуализации и аналитики данных.

Содержит функции для создания графиков распределения классов
и анализа результатов классификации.
"""

from pathlib import Path
from typing import Optional
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def plot_class_distribution(
    y: np.ndarray,
    class_names: list[str],
    save_path: Optional[Path] = None,
    title: str = "Распределение классов уровня специалиста",
) -> None:
    """
    Создает столбчатую диаграмму распределения классов.

    Аргументы:
        y: Массив меток классов.
        class_names: Список названий классов.
        save_path: Путь для сохранения графика. Если None, график не сохраняется.
        title: Заголовок графика.
    """
    class_counts = Counter(y)
    counts = [class_counts[i] for i in range(len(class_names))]
    percentages = [count / sum(counts) * 100 for count in counts]

    plt.style.use("seaborn-v0_8-darkgrid")
    _, ax = plt.subplots(figsize=(12, 7))

    colors = ["red", "yellow", "green"]
    bars = ax.bar(
        class_names, counts, color=colors, alpha=0.85, edgecolor="black", linewidth=1.5
    )

    for bar, count, pct in zip(bars, counts, percentages):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + max(counts) * 0.02,
            f"{count}\n({pct:.1f}%)",
            ha="center",
            va="bottom",
            fontsize=13,
            fontweight="bold",
            color="#333333",
        )

    ax.set_xlabel(
        "Уровень специалиста", fontsize=15, fontweight="bold", color="#333333"
    )
    ax.set_ylabel("Количество резюме", fontsize=15, fontweight="bold", color="#333333")
    ax.set_title(title, fontsize=17, fontweight="bold", color="#1a1a1a", pad=20)
    ax.grid(axis="y", alpha=0.4, linestyle="--", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1.5)
    ax.spines["bottom"].set_linewidth(1.5)

    plt.tight_layout()

    if save_path:
        save_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"График сохранен: {save_path}")
    else:
        plt.show()

    plt.close()


def analyze_class_balance(y: np.ndarray, class_names: list[str]) -> dict[str, any]:
    """
    Анализирует баланс классов в данных.

    Аргументы:
        y: Массив меток классов.
        class_names: Список названий классов.

    Вернет:
        Словарь с результатами анализа, включая counts, percentages,
        imbalance_ratio и is_balanced.
    """
    class_counts = Counter(y)
    counts = [class_counts[i] for i in range(len(class_names))]
    total = sum(counts)
    percentages = [count / total * 100 for count in counts]

    max_count = max(counts)
    min_count = min(counts)
    imbalance_ratio = max_count / min_count if min_count > 0 else float("inf")

    is_balanced = imbalance_ratio < 1.5

    return {
        "counts": dict(zip(class_names, counts)),
        "percentages": dict(zip(class_names, percentages)),
        "total": total,
        "imbalance_ratio": imbalance_ratio,
        "is_balanced": is_balanced,
    }
