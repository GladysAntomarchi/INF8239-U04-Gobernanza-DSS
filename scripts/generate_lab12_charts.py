
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Archivos originales del LAB12
BASE = Path("reports/lab12")
OUTPUT = BASE / "graficos"
OUTPUT.mkdir(parents=True, exist_ok=True)


def load_metrics(model):
    path = BASE / model / "global_metrics.json"
    with path.open(encoding="utf-8") as file:
        return json.load(file)


logistic = load_metrics("logistic")
tree = load_metrics("tree")

# ==========================================
# GRAFICO 1: BRECHAS DE EQUIDAD
# ==========================================

metrics = ["recall", "fpr", "selection_rate"]
labels = ["Recall", "FPR", "Tasa de seleccion"]

logistic_values = [
    logistic["differences"][metric] * 100
    for metric in metrics
]

tree_values = [
    tree["differences"][metric] * 100
    for metric in metrics
]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 5))

bars1 = ax.bar(
    x - width / 2,
    logistic_values,
    width,
    label="Logistic",
    color="#2563EB"
)

bars2 = ax.bar(
    x + width / 2,
    tree_values,
    width,
    label="Tree",
    color="#F59E0B"
)

ax.set_title("Brechas de equidad entre grupos")
ax.set_ylabel("Diferencia absoluta (puntos porcentuales)")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.grid(axis="y", alpha=0.2)

ax.bar_label(bars1, fmt="%.1f")
ax.bar_label(bars2, fmt="%.1f")

fig.tight_layout()

fig.savefig(
    OUTPUT / "brechas_equidad.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

# ==========================================
# GRAFICO 2: DESEMPENO GLOBAL
# ==========================================

metrics = ["accuracy", "recall", "precision"]
labels = ["Accuracy", "Recall", "Precision"]

logistic_values = [
    logistic["metrics"][metric] * 100
    for metric in metrics
]

tree_values = [
    tree["metrics"][metric] * 100
    for metric in metrics
]

x = np.arange(len(labels))

fig, ax = plt.subplots(figsize=(9, 5))

bars1 = ax.bar(
    x - width / 2,
    logistic_values,
    width,
    label="Logistic",
    color="#2563EB"
)

bars2 = ax.bar(
    x + width / 2,
    tree_values,
    width,
    label="Tree",
    color="#F59E0B"
)

ax.set_title("Comparacion del desempeno global")
ax.set_ylabel("Porcentaje (%)")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylim(0, 100)
ax.legend()
ax.grid(axis="y", alpha=0.2)

ax.bar_label(bars1, fmt="%.1f")
ax.bar_label(bars2, fmt="%.1f")

fig.tight_layout()

fig.savefig(
    OUTPUT / "desempeno_global.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)

print("Graficos generados correctamente:")
print(OUTPUT / "brechas_equidad.png")
print(OUTPUT / "desempeno_global.png")
