
import json
from pathlib import Path

import matplotlib.pyplot as plt

# Leer resultados reales del LAB13
source = Path("reports/lab13/deployment_decision.json")

with source.open(encoding="utf-8") as file:
    data = json.load(file)

checks = data["decision"]["checks"]

labels = {
    "recall": "Recall",
    "recall_gap": "Brecha de recall",
    "fpr_gap": "Brecha de FPR",
    "latency": "Latencia",
    "model_size": "Tamaño del modelo",
}

names = [labels[key] for key in labels]
values = [1 if checks[key] else 0 for key in labels]

fig, ax = plt.subplots(figsize=(9, 4.5))

bars = ax.barh(
    names,
    values,
    color=["#26866C" if passed else "#C45656"
           for passed in values],
    height=0.55,
)

for bar, passed in zip(bars, values):
    ax.text(
        0.5,
        bar.get_y() + bar.get_height() / 2,
        "CUMPLE" if passed else "NO CUMPLE",
        ha="center",
        va="center",
        color="white",
        fontweight="bold",
    )

ax.set_xlim(0, 1.05)
ax.set_xticks([])
ax.invert_yaxis()
ax.set_title(
    "Cumplimiento de puertas técnicas del DSS",
    fontsize=14,
    fontweight="bold",
    pad=15,
)

for spine in ax.spines.values():
    spine.set_visible(False)

fig.text(
    0.5,
    0.02,
    "Fuente: deployment_decision.json | "
    "La aprobación técnica no sustituye la autorización humana.",
    ha="center",
    fontsize=9,
)

fig.tight_layout(rect=[0, 0.05, 1, 1])

output = Path("reports/lab13/graficos")
output.mkdir(parents=True, exist_ok=True)

fig.savefig(
    output / "puertas_gobernanza.png",
    dpi=300,
    bbox_inches="tight",
)

plt.close(fig)

print("Gráfico generado correctamente:")
print(output / "puertas_gobernanza.png")
